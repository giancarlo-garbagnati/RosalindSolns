"""

"""

# Building file name
probnum = 'mrna'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

data_input = open(filename, 'r')
in_file = [x.replace('\n','') for x in data_input.readlines()]
protein = in_file[0]

# Derived from the soln to 01_mi_prot.py
codon_dict = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 
            'GUC': 'V', 'UUA': 'L', 'CUA': 'L', 'AUA': 'I','GUA': 'V', 'UUG': 'L', 'CUG': 'L', 
            'AUG': 'M', 'GUG': 'V', 'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 
            'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 
            'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 
            'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'UAA': 'Stop', 'CAA': 'Q', 
            'AAA': 'K', 'GAA': 'E','UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'UGU': 'C', 
            'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G', 
            'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'UGG': 'W', 'CGG': 'R', 
            'AGG': 'R', 'GGG': 'G'}
# We'll go through just the values, and create a new dict with the protein and a codon count
protein_ltr_dict = dict()
for protein_ltr in codon_dict.values():
    if protein_ltr not in protein_ltr_dict:
        protein_ltr_dict[protein_ltr] = 1
    else:
        protein_ltr_dict[protein_ltr] = protein_ltr_dict[protein_ltr] + 1

# Traverse through each aa of the protein and determine the number of potential combinations
combinations = protein_ltr_dict[protein[0]] # grab the first aa and start with that
for aa in protein[1:]:
    combinations *= protein_ltr_dict[aa]
combinations *= protein_ltr_dict['Stop'] # For stop codon/s

modulo_combinations = combinations % int(1e6)
print(modulo_combinations)

