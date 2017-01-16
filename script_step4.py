#/usr/bin/python2.4
#
#
import psycopg2
import psycopg2.extras
from collections import defaultdict
import sys
# Try to connect
#help(psycopg2.connect)

try:
    conn = psycopg2.connect("host='localhost' port='1999' dbname='dblp' user='bds16s0' password='postgres'")
except:
    print "Failed to open connection"

# Create a cursor
# The dict cursors allow to access to the retrieved records using an interface similar to the Python dictionaries instead of the tuples.
# Othewise tuple indices must be integers.
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Set the number of rows fetched at one time from the server
cur.itersize = 50

# Prepare and execute a query
try:
    cur.execute("""select * from a2;""")
	
except:
    print "Failed to execute query"

# Iterate and process the query results
# A['2017']['challeng']['5'] = 9
# dictionnaire (kw) de listes de tuples (2017, freq)
A = {}
for row in cur:
	if str(row[0]) not in A:
		A[str(row[0])] = {}
	if str(row[1]) not in A[str(row[0])]:
		A[str(row[0])][str(row[1])] = {}
	if str(row[2]) not in A[str(row[0])][str(row[1])]:
		A[str(row[0])][str(row[1])][str(row[2])] = row[3]

d = {}
freq = 0.0
sum = 0.0
# 2017, 2016...
for year in A.keys():
	# keyword
	if year != 'None':
		for num_coauthors in A[str(year)]['None'].keys():
			if num_coauthors != 'None':
				if num_coauthors not in d:
					d[str(num_coauthors)] = list()
				sum = A['None']['None'][str(num_coauthors)]
				freq = (float)(A[str(year)]['None'][str(num_coauthors)])/(float)(sum)
				sum = 0.0
				d[str(num_coauthors)].append((str(year), freq))

distance = {}
for keyword, pairs in d.items():
	n = len(pairs)
	c = 0
	for year, freq in pairs:
		c += (freq - 1./n)**2
	distance[keyword] = c

k = int(sys.argv[1])
top_k = []
i = 0
for kw, dist in sorted(distance.items(), key = lambda x: x[1], reverse = True):
	i += 1
	top_k.append(kw)
	if i >= k:
		break

print(top_k)

def save_data(dic, k):
	f = open('freq' + str(k) + '_coauthors' + '.dat', 'w')
	for year, freq in sorted(dic):
		f.write(str(year) + '\t' + str(freq) + '\n')
	f.close()

for k, s in enumerate(top_k):
	save_data(d[s], k+1)
	
cur.close()
conn.close()
