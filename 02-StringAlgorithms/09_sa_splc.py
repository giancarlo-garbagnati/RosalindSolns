"""
http://rosalind.info/problems/splc/
Genes are Discontiguous
Problem
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
Sample Output
MVYIADKQHVASREAYGHMFKVCA
"""

#imports
import re

# Building file name
probnum = 'splc'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

# Parse out all the label/dna pairs from the file into a dictionary
def fasta_to_dict(filename):
    # read file, and sort into a list of lines
    data_input = open(filename, 'r')
    in_file = [x.replace('\n','') for x in data_input.readlines()]

    fasta_dict = dict()

    dna_s = ''
    for i, line in enumerate(in_file):
        # label
        if line[0] == '>':
            label = line[1:]
        # dna
        else:
            dna_s += line
            # next line is a new dna
            if (i+1 < len(in_file)) and (in_file[i+1][0] == '>'):
                fasta_dict[label] = dna_s
                dna_s = ''
    fasta_dict[label] = dna_s

    return fasta_dict

# Derived from the soln to 01_mi_prot.py
codon_dict = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 
            'GUC': 'V', 'UUA': 'L', 'CUA': 'L', 'AUA': 'I','GUA': 'V', 'UUG': 'L', 'CUG': 'L', 
            'AUG': 'M', 'GUG': 'V', 'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 
            'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 
            'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 
            'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'UAA': 'Stop', 'CAA': 'Q', 
            'AAA': 'K', 'GAA': 'E', 'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'UGU': 'C', 
            'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G', 
            'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'UGG': 'W', 'CGG': 'R', 
            'AGG': 'R', 'GGG': 'G'}

# Using this isn't probably the most optimal, but since it already exists, I'll use this
# and pull out the other information seperately
fasta_dict = fasta_to_dict(filename)

# Let's read the file's first entry to get the name of the main DNA string
data_in = open(filename, 'r')
data_lines = [x.replace('\n','') for x in data_in.readlines()]
dna_s_key = data_lines[0][1:]
dna_s = fasta_dict[dna_s_key]

# Get a list of all introns
introns = [fasta_dict[key] for key in fasta_dict.keys() if key != dna_s_key]

# Build a dict of intron start index, intron sequence as key, value
# This makes (maybe a dangerous) assumption that each intron are unique or aren't in parts of other
# introns
intron_dict = {}
intron_indices = []
for intron in introns:
    intron_index_list = [intron_index.start() for intron_index in re.finditer(intron.upper(), dna_s)]
    intron_indices += intron_index_list
    for intron_index in intron_index_list:
        intron_dict[intron_index] = intron
intron_indices.sort(reverse=True)

# Go through each intron index, and remove that intron from the spliced DNA
spliced_s = dna_s
for intron_index in intron_indices:
    spliced_s = spliced_s.replace(intron_dict[intron_index],'')

# Translate DNA to RNA, then to protein
spliced_s = spliced_s.replace('T','U')
protein = ''
for i in range(0, len(spliced_s), 3):
    codon = spliced_s[i:i+3]
    if codon_dict[codon] == 'Stop':
        break
    protein += codon_dict[codon]

print(protein)
