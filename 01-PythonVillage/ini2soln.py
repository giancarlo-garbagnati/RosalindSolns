"""
Variables and Some Arithmetic
Problem
Given: Two positive integers aa and bb, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths aa and bb.

Sample Dataset
3 5
Sample Output
34
"""

from math import sqrt

probnum = 'ini2'
filename = '../data/rosalind_' + probnum + '.txt'

data_input = open(filename, 'r')
data_input = data_input.read().replace('\n','')

nums = data_input.split()

a = int(nums[0])
b = int(nums[1])

c_sq = a**2 + b**2

print(a,b)
print(c_sq)