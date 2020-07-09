#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
for nt in range(len(dna)-1,-1,-1):
	if   dna[nt] == 'T': print('A', end='')
	elif dna[nt] == 'G': print('C', end='')
	elif dna[nt] == 'C': print('G', end='')
	else:		  	     print('T', end='')





#fail#1
#neil's
#print("".join([dna[i] for i in range(len(dna)-1,-1,-1)]))

#tasha's
# revdna = ''
# print(len(dna))
# for i in range(len(dna)-1,-1,-1):
# 	revdna += dna[i]
# print(revdna)
"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
