"""
http://rosalind.info/problems/ini6/
Intro to Python dictionary
Problem
Given: A string ss of length at most 10000 letters.

Return: The number of occurrences of each word in ss, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

Sample Dataset
We tried list and we tried dicts also we tried Zen
Sample Output
and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1
"""

# Building file name
probnum = 'ini6'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

# Parse out the variables from the file
data_input = open(filename, 'r')
data_string = data_input.readline().replace('\n','')
words = data_string.split()

# Build the words dict
words_dict = dict()
for word in words:
    if word in words_dict.keys():
        words_dict[word] = words_dict[word] + 1
    else:
        words_dict[word] = 1

# Go through each key/value pair in the dict and output it
for word, num in words_dict.items():
    print(word, num)
