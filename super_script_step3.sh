#!/bin/bash

python script_step3.py $1
for i in `seq 1 $1`;do
	gnuplot <<- EOF
		set term png
		set output "plot${i}_kw.png"
		plot "freq${i}_kw.dat" with linespoints ls 1	
	EOF
done
