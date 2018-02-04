"""
Conditions and Loops
Problem
Given: Two positive integers aa and bb (a<b<10000a<b<10000).

Return: The sum of all odd integers from aa through bb, inclusively.

Sample Dataset
100 200
Sample Output
7500
"""

# Building file name
probnum = 'ini4'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

# Parse out the variables from the file
data_input = open(filename, 'r')
data_string = data_input.readline().replace('\n','')
nums = [int(x) for x in data_string.split()]

# Loop through all numbers, only adding to soln if odd
soln = 0
for i in range(nums[0],nums[1]+1):
    if i%2==1:
        soln += i

print(soln)
