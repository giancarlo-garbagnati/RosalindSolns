"""
http://rosalind.info/problems/cons/
The Billion-Year War
Problem

Figure 2. Palindromic recognition site
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""

# Building file name
probnum = 'revp'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

# Parse out the variables from the file
data_input = open(filename, 'r')
fasta_file = [x.replace('\n','') for x in data_input.readlines()]
seq = ''
for line in fasta_file:
    if line[0] == '>':
        label = line[1:]
    else:
        seq += line
min_pal = 4
max_pal = 12

# Function to determine if a string is a DNA palindromic sequence, only takes even length'd sequences
def is_dna_palindrome(dna_s):
    l = len(dna_s)
    hl = int(l/2)
    if l%2==1: # odd length sequence = False
        return False
    
    return dna_s[:hl] == revc(dna_s[hl:])

# Function that returns a DNA sequence's reverse compliment
def revc(dna_s):
    dna_s = dna_s.upper().replace('A','X').replace('T','A').replace('X','T')
    dna_s = dna_s.replace('G','X').replace('C','G').replace('X','C')
    return dna_s[::-1]

# Function to return a list of tuples (location, length) and of all DNA palindromes of a given length
def find_all_dna_palindromes(dna_s, pal_len):
    pal_list = []
    for i in range(pal_len,len(dna_s)+1):
        current = dna_s[i-pal_len:i]
        if is_dna_palindrome(current):
            pal_list.append((i-pal_len+1, pal_len))
    return pal_list

# Go through all 4-12 and find all palindromes of each length, and combine them in one list
all_pals = []
for i in range(min_pal,max_pal+1):
    all_pals = all_pals + find_all_dna_palindromes(seq, i)

for pair in all_pals:
    print(pair[0], pair[1])
