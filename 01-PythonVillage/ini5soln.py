"""
Reading and Writing
Problem
Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

Sample Dataset
Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat
Sample Output
Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat
"""

# Building file name
probnum = 'ini5'
filename = '../data/rosalind_' + probnum
filein_str = filename + '.txt'
#filein_str = filename + '_sample.txt'

# Parse out the variables from the file
filein = open(filein_str, 'r')
data_string = filein.readlines()

# Build output str
fileout_str = filename + '_soln.txt'
fileout = open(fileout_str, 'w')
for i in range(0, len(data_string)):
    if i%2==1: # We want even lines, but since we're using 1-based numbering for lines, we look for odd numbered lines
        fileout.write(data_string[i])


