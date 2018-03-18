"""
http://rosalind.info/problems/revc/
The Secondary and Tertiary Structures of DNA
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string ss is the string scsc formed by reversing the symbols of ss, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string ss of length at most 1000 bp.

Return: The reverse complement scsc of ss.

Sample Dataset
AAAACCCGGT
Sample Output
ACCGGGTTTT
"""

# Building file name
probnum = 'revc'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

# Parse out the variables from the file
data_input = open(filename, 'r')
dna_seq = data_input.readline().replace('\n','')

# First let's reverse the DNA seq
revc_dna = dna_seq[::-1]

# Now let's do the replacements
# First A<->T
revc_dna = revc_dna.replace('A','X').replace('T','A').replace('X','T')
# Now G<->C
revc_dna = revc_dna.replace('G','X').replace('C','G').replace('X','C')

print(revc_dna)