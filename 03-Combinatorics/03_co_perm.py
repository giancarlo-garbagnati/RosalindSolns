"""
http://rosalind.info/problems/perm/
Rearrangements Power Large-Scale Genomic Changes
Problem
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

Sample Dataset
3
Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

# Imports
from math import factorial

# Building file name
probnum = 'perm'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

data_input = open(filename, 'r')
in_file = [x.replace('\n','') for x in data_input.readlines()]

n = int(in_file[0])
total_perms = factorial(n)

n_choices = [x+1 for x in range(0,n)]

# Helper function to swap values at specific indices of a list
def swap_values(l, i, j):
    l = [x for x in l]
    j_temp = l[i]
    l[i] = l[j]
    l[j] = j_temp
    return l

# Recursive function to go through a list of values and return a list of lists of all possible
# permutations
def perm_recursion(l):
    if len(l) == 1:
        return [l]
    all_perms = []
    for i in range(0,len(l)):
        swapped = swap_values(l, 0, i)
        lower_perms = perm_recursion(swapped[1:])
        current_perms = [(swapped[:1] + li) for li in lower_perms]
        all_perms = all_perms + current_perms
    return all_perms

permutations = perm_recursion(n_choices)

print(total_perms)
for permutation in permutations:
    for value in permutation:
        print(value, end=' ')
    print()

