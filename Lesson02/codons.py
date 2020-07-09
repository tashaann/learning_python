#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'
"""
i = 0 
while i < len(dna):
	print(dna[i:i+3], i)
	i += 3
"""
for j in range(3):
	for i in range(j,len(dna)-2,3): #len seq - word size + 1
		print(dna[i:i+3], i)
	print()

"""
python3 codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
