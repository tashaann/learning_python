#!/usr/bin/env python3

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

# Write a program that computes the GC% of a DNA sequence
GC_comp = 0


for nt in range(len(dna)):
	if   dna[nt] == 'G' or dna[nt] == 'C': GC_comp += 1
	else: continue

# Format the output for 2 decimal places
# Use all three formatting methods
# Method 1: printf()
print('%.2f' % (GC_comp/len(dna)))

# Method 2: str.format()
print('{:.2f}'.format(GC_comp/len(dna)))

# Method 3: f-strings
print(f'{GC_comp/len(dna):.2f}')
"""
python3 gc.py
0.42
0.42
0.42
"""
