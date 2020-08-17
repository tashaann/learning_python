#!/usr/bin/env python3

import fileinput

# Write a program that computes typical sequence stats
# No, you cannot import any other modules!
# Use rand_seq to generate the sequences
# Expected output is shown below

# check id length generated is 0 or do an assert to not choose lenth 1 as min length
# make a dictonary with lenth being the value?

# variables 
numlet = 0 
sumseqlen = 0
nt_A = 0
nt_C = 0
nt_G = 0
nt_T = 0

# data = [ seq1:len(seq1), ...]
data = []

# reading through "fasta file"
for line in fileinput.input():
	if line.startswith('>'): continue
	line = line.rstrip()
	data.append([line, len(line)])


# sort my by seq length to get max and min length 
data = sorted(data, key=lambda x: x[1])


# so in data, be able to iterate througth each string, identify which nt and count those. 
# seq length


sumLengths = sum([x[1] for x in data])
# to get numer of letters


# N50
for seq in data:
	if sumseqlen < 0.5*sumLengths: sumseqlen += seq[1]
	else:
		N50 = seq[1]-1
		break


# Composition
for i in range(len(data)):
	seq = data[i][0]
	for nt in seq:
		if nt == 'A':  nt_A += 1
		elif nt == 'C': nt_C += 1
		elif nt == 'G': nt_G += 1
		else:
			nt_T += 1
	#print(nt_A)


nt_comp = [nt_A/sumLengths, nt_C/sumLengths, nt_G/sumLengths, nt_T/sumLengths]


#priny statements
print('{} {}'.format('Number of sequence:',len(data)))
print('{} {}'.format('Number of letters:', sumLengths))
print('{} {}'.format('Minimum length:',data[0][1]))
print('{} {}'.format('Maximum length:',data[-1][-1]))
print('{} {}'.format('N50:', N50 ))
print('%s %s%.3f %s%.3f %s%.3f %s%.3f' % ('Composition:', 'A=', nt_comp[0],'C=', nt_comp[1], 'G=', nt_comp[2], 'T=', nt_comp[3]))
"""
python3 rand_seq.py 100 100 100000 0.35 | python3 seqstats.py
Number of sequences: 100
Number of letters: 4957689
Minimum length: 219
Maximum length: 99853
N50: 67081
Composition: A=0.325 C=0.175 G=0.175 T=0.325
"""
