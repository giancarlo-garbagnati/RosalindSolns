"""
http://rosalind.info/problems/hamm/
Evolution as a Sequence of Mistakes
Problem

Given two strings ss and tt of equal length, the Hamming distance between ss and tt, denoted dH(s,t)dH(s,t), is the number of corresponding symbols that differ in ss and tt. See Figure 2.

Given: Two DNA strings ss and tt of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)dH(s,t).

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample Output
7
"""

# Building file name
probnum = 'hamm'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

# Parse out the variables from the file
data_input = open(filename, 'r')
in_file = [x.replace('\n','') for x in data_input.readlines()]

s = in_file[0]
t = in_file[1]

hamming_distance = 0
for i in range(0,len(s)):
    if s[i] != t[i]:
        hamming_distance += 1

print(hamming_distance)
