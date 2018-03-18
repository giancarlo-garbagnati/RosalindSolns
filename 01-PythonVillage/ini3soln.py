"""
http://rosalind.info/problems/ini3/
Strings and lists
Problem
Given: A string ss of length at most 200 letters and four integers aa, bb, cc and dd.

Return: The slice of this string from indices aa through bb and cc through dd (with space in between), inclusively. In other words, we should include elements s[b]s[b] and s[d]s[d] in our slice.

Sample Dataset
HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102
Sample Output
Humpty Dumpty
"""

# Building file name
probnum = 'ini3'
filename = '../data/rosalind_' + probnum + '.txt'

# Parse out the variables from the file
data_input = open(filename, 'r')
data_string = data_input.readline().replace('\n','')
data_indices_str = data_input.readline().replace('\n','')
data_indices = [int(x) for x in data_indices_str.split()]

# Let's get both slices
slice_a = data_string[data_indices[0]:data_indices[1]+1]
slice_b = data_string[data_indices[2]:data_indices[3]+1]

# Let's build submission output
soln = slice_a + ' ' + slice_b

print(soln)
