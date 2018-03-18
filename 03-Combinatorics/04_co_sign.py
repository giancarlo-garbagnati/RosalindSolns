"""
http://rosalind.info/problems/sign/
Synteny Blocks Have Orientations
Problem
A signed permutation of length n is some ordering of the positive integers {1,2,…,n} in which each integer is then provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example, π=(5,−3,−2,1,4) is a signed permutation of length 5.

Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).

Sample Dataset
2
Sample Output
8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1
"""

# We can reuse most of the code from '03_co_perm', and then 

# Imports
from math import factorial

# Building file name
probnum = 'sign'
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

# From 03_co_perm solution
'''
print(total_perms)
for permutation in permutations:
    for value in permutation:
        print(value, end=' ')
    print()
'''

# generate a list of all binary numbers
tform_list = []
for i in range(0,2**n):
    bin_i = list(str(bin(i)))[2:]
    bin_i = [-1 if int(x) is 0 else int(x) for x in bin_i]
    bin_i = ([-1]*(n - len(bin_i))) + bin_i
    tform_list.append(bin_i)

num_signed_permutations = total_perms*len(tform_list)
print(num_signed_permutations)

# element-wise multiplication for each permutation-transformation pair
signed_permutations = []
for permutation in permutations:
    for tform in tform_list:
        signed_perm = [a*b for a,b in zip(permutation,tform)]
        signed_permutations.append(signed_perm)
        for value in signed_perm:
            print(value, end=' ')
        print()

# run in shell as:
# > python 04_co_sign.py > 04_co_sign.py.output.txt
