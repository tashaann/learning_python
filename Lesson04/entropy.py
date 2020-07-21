#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# Use fileinput to get the data from nucleotides.txt
# Make sure that the values are probabilities
# Make sure that the distribution sums to 1
# Report with 3 decimal figures

import fileinput
import math


data = []
pi_sum = 0

for line in fileinput.input():
	if line.startswith('#'): continue
	line = line.rstrip()
	l = line.split(' ')
	data.append(float(l[1])) 
for i in data:
	pi_sum = pi_sum -(i*math.log2(i))

print(f'{pi_sum:.3f}')


"""
python3 entropy.py nucleotides.txt
1.846
"""
