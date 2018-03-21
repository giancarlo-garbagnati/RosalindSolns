"""
http://rosalind.info/problems/mprt/
Motif Implies Function
Problem
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into

http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following

http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""

# Building file name
probnum = 'mprt'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

data_input = open(filename, 'r')
in_file = [x.replace('\n','') for x in data_input.readlines()]
#couples_list = [int(x) for x in in_file[0].split(' ')]

#from urllib import request
from urllib.request import urlopen

def search_for_n_glycosylation(uniprotID):
    # Read in the protein from online (uniprot)
    url = 'http://www.uniprot.org/uniprot/{}.fasta'.format(uniprotID)
    protein = ''.join(str(urlopen(url).read()).split('\\n')[1:-1])

    # N{P}[ST]{P}
    locations = []
    for i in range(0, len(protein)):
        if (protein[i].upper() == 'N') and (i+4 <= len(protein)):
            four_letter = protein[i:i+5]
            if four_letter[1].upper() != 'P':
                if four_letter[2].upper() in ['S','T']:
                    if four_letter[3].upper() != 'P':
                        locations.append(i+1)
    
    return uniprotID,locations

# Go through each protein and check for the motif (and where)
protein_dict = dict()
for proteinID in in_file:
    _, motif_locations = search_for_n_glycosylation(proteinID)
    protein_dict[proteinID] = motif_locations
    if len(motif_locations) > 0:
        print(proteinID)
        for location in motif_locations:
            print(location, end = ' ')
        print()

