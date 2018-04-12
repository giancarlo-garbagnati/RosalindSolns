"""
http://rosalind.info/problems/orf/
Transcription May Begin Anywhere
Problem
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""

#imports
import re

# Building file name
probnum = 'orf'
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

fasta_dict = fasta_to_dict(filename)
for dna in fasta_dict.values():
    dna_s = dna.upper().replace('T','U')
revc_s = dna_s.replace('A','X').replace('U','A').replace('X','U').replace('C','X').replace('G','C').replace('X','G')[::-1]

# find all occurances of the start codon 'AUG' <- start of each orf
orig_start = [start_codon.start() for start_codon in re.finditer('AUG',dna_s)]
revc_start = [start_codon.start() for start_codon in re.finditer('AUG',revc_s)]

# function to add all translated proteins to the protein list
def find_and_translate_all_orfs(dna_sequence, orf_indices, translated_protein_list):
    for orf_i in orf_indices:
        protein = ''
        for i in range(orf_i, len(dna_sequence[orf_i:]) + orf_i, 3):
            if i+2 <= len(dna_sequence):
                codon = dna_sequence[i:i+3]
                if codon_dict[codon] == 'Stop': # stop codon, we add the translated protein to the list, and move to the next orf
                    if protein not in translated_protein_list: # check to not add duplicates
                        translated_protein_list.append(protein)
                    break
                else: # translate the codon and add it to the growing protein peptide
                    protein += codon_dict[codon]

# go through each orf, and translate until you get to a stop codon
protein_strings = []
find_and_translate_all_orfs(dna_s, orig_start, protein_strings)
find_and_translate_all_orfs(revc_s, revc_start, protein_strings)

for protein in protein_strings:
    print(protein)


