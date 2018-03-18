"""
http://rosalind.info/problems/revp/
Finding a Most Likely Common Ancestor
Problem
A matrix is a rectangular table of values divided into rows and columns. An m×nm×n matrix has mm rows and nn columns. Given a matrix AA, we write Ai,jAi,j to indicate the value found at the intersection of row ii and column jj.

Say that we have a collection of DNA strings, all having the same length nn. Their profile matrix is a 4×n4×n matrix PP in which P1,jP1,j represents the number of times that 'A' occurs in the jjth position of one of the strings, P2,jP2,j represents the number of times that C occurs in the jjth position, and so on (see below).

A consensus string cc is a string of length nn formed from our collection by taking the most common symbol at each position; the jjth symbol of cc therefore corresponds to the symbol having the maximum value in the jj-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

A T C C A G C T
G G G C A A C T
A T G G A T C T
DNA Strings	A A G C A A C C
T T G G A A C T
A T G C C A T T
A T G G C A C T
A   5 1 0 0 5 5 0 0
Profile	C   0 0 1 4 2 0 6 1
G   1 1 6 3 0 1 0 0
T   1 5 0 0 0 1 1 6
Consensus	A T G C A A C T
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""

# Building file name
probnum = 'cons'
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
fasta_list = list(fasta_dict.values())

# given a string, returns the consensus and number of each nucleotid
def count_nts(s):
    nts = {
        'a':0,
        'c':0,
        'g':0,
        't':0
    }
    a = 0
    c = 0
    g = 0
    t = 0
    
    for nt in s:
        if nt == 'A':
            a += 1
        elif nt == 'C':
            c += 1
        elif nt == 'G':
            g += 1
        elif nt == 'T':
            t += 1

    consensus = ['A','C','G','T'][[a,c,g,t].index(max([a,c,g,t]))]
    return consensus,a,c,g,t

# Go through each i-th index of each sequence, get the profile and consensus
seq_len = len(fasta_list[0])
consensus = ''
a = []
c = []
g = []
t = []
for i in range(0,seq_len):
    ith_nts = ''
    for seq in fasta_list:
        ith_nts += seq[i]
    i_consensus, i_a, i_c, i_g, i_t = count_nts(ith_nts)
    consensus += i_consensus
    a.append(i_a)
    c.append(i_c)
    g.append(i_g)
    t.append(i_t)

# format output
print(consensus)
a_str = 'A: '
c_str = 'C: '
g_str = 'G: '
t_str = 'T: '
for n in a:
    a_str += str(n) + ' '
a_str = a_str[:-1]
for n in c:
    c_str += str(n) + ' '
c_str = c_str[:-1]
for n in g:
    g_str += str(n) + ' '
g_str = g_str[:-1]
for n in t:
    t_str += str(n) + ' '
t_str = t_str[:-1]
print(a_str)
print(c_str)
print(g_str)
print(t_str)

