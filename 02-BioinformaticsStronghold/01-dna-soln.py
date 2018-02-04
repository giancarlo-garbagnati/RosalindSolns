"""
A Rapid Introduction to Molecular Biology
Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string ss of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.

Sample Dataset
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
Sample Output
20 12 17 21
"""

# Building file name
probnum = 'dna'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

# Parse out the variables from the file
data_input = open(filename, 'r')
dna_seq = data_input.readline().replace('\n','').lower()

# Instantiate the nucleotide count dictionary
nt_count = {
    'a':0,
    'c':0,
    'g':0,
    't':0
}
# Loop through the DNA seq, and count each NT
for nt in dna_seq:
    nt_count[nt] = nt_count[nt] + 1

print(nt_count['a'], nt_count['c'], nt_count['g'], nt_count['t'])
