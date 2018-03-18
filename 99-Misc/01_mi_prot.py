"""
http://rosalind.info/problems/prot/
The Genetic Code
Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
Sample Output
MAMAPRTEINSTRING
"""

# Building file name
probnum = 'prot'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

data_input = open(filename, 'r')
in_file = [x.replace('\n','') for x in data_input.readlines()]
rna_string = in_file[0]

# From http://rosalind.info/glossary/rna-codon-table/
codon_str = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

# Convert that codon string into a dictionary where each RNA codon triplet is the key and the
#  value is the protein 1-letter translation
codons = codon_str.split('\n')
codon_dict = dict()
for four_codons_str in codons:
    for codon in four_codons_str.split('   '):
        if len(codon) < 1:
            continue
        codon_prot_pair = codon.split(' ')
        codon_dict[codon_prot_pair[0]] = codon_prot_pair[1]

""" For the future:
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
"""

# We walk through the RNA string and translate each codon triplet until we get to a STOP codon
if len(rna_string) > 3:
    still_more_to_translate = True
else:
    still_more_to_translate = False
i = 0
protein = ''
while still_more_to_translate:
    end = i+3

    codon = rna_string[i:end]
    translation = codon_dict[codon]

    # Check to see if we have a stop codon, then we stop translating
    if translation.lower() == 'stop':
        still_more_to_translate = False
        break
    else:
        protein += translation

    # Sanity check to see if we're running out of RNA to translate
    if len(rna_string) <= end+2:
        still_more_to_translate = False
    else:
        i += 3

print(protein)