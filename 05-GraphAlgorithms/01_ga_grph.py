"""
A Brief Introduction to Graph Theory
Problem
A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).

For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

Sample Dataset
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
Sample Output
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""

# Building file name
probnum = 'grph'
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

fasta_dict = fasta_to_dict(filename)
# O of 3, so k = 3
k = 3

# Loop through each DNA string and check if it is an edge with all other nucleotides
adjacency_edges = []
for key_i, value_i in fasta_dict.items():
    for key_j, value_j in fasta_dict.items():
        if value_i != value_j:
            if fasta_dict[key_i][-k:] == fasta_dict[key_j][:k]:
                output = "{} {}".format(key_i, key_j)
                print(output)
                adjacency_edges.append(output)

