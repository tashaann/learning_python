#!/usr/bin/env python3

import gzip
import sys
import math
import random

# Write a program that creates random fasta files
# Create a function that makes random DNA sequences
# Parameters include length and frequencies for A, C, G, T
# Command line:
#	python3 rand_fasta.py <count> <min> <max> <a> <c> <g> <t>
# try using argparse instead of assert


seq_num = int(sys.argv[1])
min_len = int(sys.argv[2])
max_len = int(sys.argv[3])
fA = float(sys.argv[4])
fC = float(sys.argv[5])
fG = float(sys.argv[6])
fT = float(sys.argv[7])

frq = fA + fC + fG + fT
print(type(frq), frq, fA, fC,fG,fT)
nt = ['A', 'C', 'G', 'T']


assert(seq_num > 0)
assert(min_len > 0)
assert(max_len > 0)
assert(math.isclose(frq, 1 , abs_tol = 0.01)) # sum of frq should be between 0.99 and 1.01
assert(fA > 0 and fA < 1)
assert(fC > 0 and fC < 1)
assert(fG > 0 and fG < 1)
assert(fT > 0 and fT < 1)




for seq in range(seq_num):
	print('{}{}'.format('>seq-',seq))
	seq_len = random.randint(min_len, max_len)
	seq_list = []
	seq_str = ''
	for nt_num in range(seq_len):
		if nt_num == seq_len - 1 :print(seq_str)
		elif nt_num < seq_len - 1:
			seq_list+=random.choices(nt, weights = (fA, fC, fG, fT) ) 
			seq_str += seq_list[nt_num]


"""
python3 rand_fasta.py 3 10 20 0.1 0.2 0.3 0.4
>seq-0
TCGTTTTGATTACGG
>seq-1
CGGCTGTTCCGTAATGC
>seq-2
TTTCGTGTACTTTCTAGTGA
"""
