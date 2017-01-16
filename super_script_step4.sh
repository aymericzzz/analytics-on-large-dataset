#!/bin/bash

python script_step4.py $1
for i in `seq 1 $1`;do
	gnuplot <<- EOF
		set term png
		set output "plot${i}_coauthors.png"
		plot "freq${i}_coauthors.dat" with linespoints ls 1	
	EOF
done
