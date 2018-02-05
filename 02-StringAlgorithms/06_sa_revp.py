"""
Combing Through the Haystack
Problem
Given two strings ss and tt, tt is a substring of ss if tt is contained as a contiguous collection of symbols in ss (as a result, tt must be no longer than ss).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position ii of ss is denoted by s[i]s[i].

A substring of ss can be represented as s[j:k]s[j:k], where jj and kk represent the starting and ending positions of the substring in ss; for example, if ss = "AUGCUUCAGAAAGGUCUUACG", then s[2:5]s[2:5] = "UGCU".

The location of a substring s[j:k]s[j:k] is its beginning position jj; note that tt will have multiple locations in ss if it occurs more than once as a substring of ss (see the Sample below).

Given: Two DNA strings ss and tt (each of length at most 1 kbp).

Return: All locations of tt as a substring of ss.

Sample Dataset
GATATATGCATATACTT
ATAT
Sample Output
2 4 10
"""

# Building file name
probnum = 'revp'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

# Parse out the variables from the file
data_input = open(filename, 'r')
fasta_file = [x.replace('\n','') for x in data_input.readlines()]
seq = fasta_file[0]
query = fasta_file[1]

# Iterate through the sequence and find all locations of the 
i = 0
query_list = []
while i >= 0:
    # We'll search from the right to left, and shorten the sequence as we find more matches
    i = seq.rfind(query)

    if i < 0:
        break
    
    seq = seq[:i+len(query)-1]
    query_list.append(i+1)

# Build output string
query_list.sort()
output = ''
for match in query_list:
    output = output + str(match) + ' '
output = output[:-1]

print(output)
