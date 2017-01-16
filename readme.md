this repo hosts python source code for connecting and retrieving data from a postgresql database hosted on a cluster.
Python scripts and shell scripts are available to do different analyze and plot some figures about the data.
The code's goal is to achieve the following 2 steps.

Step 3: Over the three dimensional array, A(year, keyword, num_coauthors: count(paper id)), discover the top-k
keywords whose popularity in paper titles changes the most significantly over years. That is, for each keyword you
are asked to find the frequency distribution over years; then find the top-k keywords whose distributions deviate the
most from the uniform distribution.
Your program should take “k” as an argument, and output k gnuplots to show the distributions of the k keywords
chosen by your program.
Step 4: Similarly, over the three dimensional array, A(year, keyword, num_coauthors: count(paper id)),
discover the top-k values of num_coauthors (e.g., 1, 9…) that have changed the most significantly over years.
Your program should take “k” as an argument, and output k gnuplots to show the distributions of the k
num_coauthors chosen by your program.
