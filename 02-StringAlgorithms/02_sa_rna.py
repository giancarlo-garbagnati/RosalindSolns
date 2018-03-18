"""
http://rosalind.info/problems/rna/
The Second Nucleic Acid
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string tt corresponding to a coding strand, its transcribed RNA string uu is formed by replacing all occurrences of 'T' in tt with 'U' in uu.

Given: A DNA string tt having length at most 1000 nt.

Return: The transcribed RNA string of tt.

Sample Dataset
GATGGAACTTGACTACGTAAATT
Sample Output
GAUGGAACUUGACUACGUAAAUU
"""

# Building file name
probnum = 'rna'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

# Parse out the variables from the file
data_input = open(filename, 'r')
dna_seq = data_input.readline().replace('\n','')

# Should be a simple replace call
print(dna_seq.replace('T','U'))
