#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Step size is 5 nt
# Output with 4 significant figures using whichever method you prefer
# Use no nested loops (as in gc_win2.py)

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
s = 5
GC_comp = 0

#why not make a list of lists? a list of the old and new GC_comp and for the seq

old_GC = []
new_GC = []
old_seq = []
new_seq = []

for i in range(w):
	if seq[i] == 'G' or seq[i] == 'C': GC_comp += 1
#print(f'{w+1} {seq[0:w]} {GC_comp/w:.4f}')

for i in range(0,len(seq)-w):
	if i%5 == 0: print(f'{i} {seq[i:i+w]} {GC_comp/w:.4f}')
	if seq[i] == 'G'  or seq[i] == 'C': GC_comp -= 1
	if seq[i+w] == 'G' or seq[i+w] == 'C': GC_comp += 1
#print(f'{i} {seq[i:i+w]} {GC_comp/w:.4f}')
	

"""
python3 gc_win4.py
0 ACGACGCAGGA 0.6364
5 GCAGGAGGAGA 0.6364
10 AGGAGAGTTTC 0.4545
15 AGTTTCAGAGA 0.3636
20 CAGAGATCACG 0.5455
25 ATCACGAATAC 0.3636
30 GAATACATCCA 0.3636
35 CATCCATATTA 0.2727
40 ATATTACCCAG 0.3636
45 ACCCAGAGAGA 0.5455
"""
