#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

data = []
count = 0
data_sum = 0 
y = 0 

# to count and get the sum
for line in fileinput.input():
	if line.startswith('#'): continue
	data.append(float(line))
	count += 1
	data_sum += data[-1]

data.sort()

minimum = data[0]

maximum = data[-1]

mean = data_sum/count

# to get median 
if count % 2 == 0:
	median = (data[count//2] + data[(count//2)-1])/2
else: 
	median = data[(count//2)-1]

# to get standard dev
for i in data:
	y += (i-mean)**2

y = sqrt(y/count)

print(f'Count: {count} \nMinimum: {minimum} \nMaximum: {maximum} \nMean: {mean} \nStd. dev: {y:.3f} \nMedian: {median}')
"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
