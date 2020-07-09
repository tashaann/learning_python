#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Step size is 5 nt
# Output with 4 significant figures using whichever method you prefer
# Use nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
s = 5
GC_comp = 0

for x in range(w):
	if seq[x] == 'G' or seq[x] == 'C': GC_comp += 1

print(f'0 {seq[:w]} {GC_comp/w:.4f}')

for i in range(0, len(seq)-10, 5):
	if i+5+w-1 >= len(seq):
		break
	for old in range(i,i+5):
		if seq[old] == 'G' or seq[old] == 'C': GC_comp -= 1
	for new in range(i+w, i+5+w):
		#print(i, new, GC_comp)
		if seq[new]	== 'G' or seq[new] == 'C': GC_comp += 1
	print(f'{i+5} {seq[i+5:i+w+5]} {GC_comp/w:.4f}')



"""
python3 gc_win3.py
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
