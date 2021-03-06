#!/usr/bin/env python3

# Create a program that generates random sequences in FASTA format
# Each name should be unique
# Length should have a minimum and maximum
# GC% should be a parameter
# Use assert() to check bounds of command line values
# When creating sequences, append and join
# Command line:
#	python3 rand_seq.py <# of seqs> <min> <max> <gc>
# do plotting
import sys
import random

seq_num = int(sys.argv[1])
min_len = int(sys.argv[2])
max_len = int(sys.argv[3])
gc_cont = float(sys.argv[4])


assert(seq_num > 0)
assert(min_len > 0)
assert(max_len > 0)
assert(gc_cont > 0 and gc_cont < 1)

# check if generating length = 0
# fix length prob.

output = 0
nt = ['A', 'C', 'G', 'T']
weights = [(1-gc_cont)/2, gc_cont/2, gc_cont/2, (1-gc_cont)/2]

for seq in range(seq_num): 
	print('{}{}'.format('>seq-',seq))
	seq_len = random.randint(min_len, max_len)
	seq_list = []
	seq_str = ''
	for nt_num in range(seq_len):
		if nt_num == seq_len-1: print(seq_str)
		elif nt_num < seq_len-1: 
			#this only give you a list so then had to convert list to string
			seq_list+=random.choices(nt, weights) 
			seq_str += seq_list[nt_num]
"""
python3 rand_seq.py 3 10 20 0.5
>seq-0
GCGCGACCTTAT
>seq-1
ATCCTAGAAGT
>seq-2
CTTCGCTCGTG
"""

