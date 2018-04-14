"""
http://rosalind.info/problems/lexf/
Organizing Strings
Problem
Assume that an alphabet 𝒜 has a predetermined order; that is, we write the alphabet as a permutation 𝒜=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z).

Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in 𝒜.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

Sample Dataset
A C G T
2
Sample Output
AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT
"""

# Building file name
probnum = 'lexf'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

data_input = open(filename, 'r')
in_file = [x.replace('\n','') for x in data_input.readlines()]
alphabet = in_file[0].split()
n = int(in_file[1])

# needs alphabet (A), n-length (subtracts with each iteration), list of permutations
def lexicographic_permutations(alphabet, n):
    
    # base case
    if n == 1:
        return alphabet

    # return all permutations of each letter in the alphabet plus all different previous
    # permutations
    new_permutations = []
    recursive_permutations = lexicographic_permutations(alphabet, n-1)
    for letter in alphabet:
        for r_permutation in recursive_permutations:
            new_permutations.append(letter+r_permutation)
    return new_permutations

all_permutations = lexicographic_permutations(alphabet, n)
list(set(all_permutations)).sort()

for permutation in all_permutations:
    print(permutation)
