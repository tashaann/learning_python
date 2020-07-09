#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time
DNA=""
AT = 0
for count in range(30):
	DNA+=random.choice("CGTTAA")
for i in range(len(DNA)):
	if DNA[i] == 'A' or DNA[i] == 'T':
		AT += 1
AT_frac = AT / len(DNA)
print(len(DNA), AT_frac, DNA)


# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence


"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
