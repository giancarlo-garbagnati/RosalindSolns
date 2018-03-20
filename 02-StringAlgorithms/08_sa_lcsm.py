"""
http://rosalind.info/problems/lcsm/
Searching Through the Haystack
Problem
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
Sample Output
AC
"""

# Building file name
probnum = 'lcsm'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

# Parse out all the label/dna pairs from the file into a dictionary
def fasta_to_dict(filename):
    # read file, and sort into a list of lines
    data_input = open(filename, 'r')
    in_file = [x.replace('\n','') for x in data_input.readlines()]

    fasta_dict = dict()

    dna_s = ''
    for i, line in enumerate(in_file):
        # label
        if line[0] == '>':
            label = line[1:]
        # dna
        else:
            dna_s += line
            # next line is a new dna
            if (i+1 < len(in_file)) and (in_file[i+1][0] == '>'):
                fasta_dict[label] = dna_s
                dna_s = ''
    fasta_dict[label] = dna_s

    return fasta_dict

fasta_dict = fasta_to_dict(filename)

# First approach:
# The longest commong substring of a collection of DNA strings can't be longer than the shortest
#  DNA sequence <--- we'll start with that one. Going from len(shortestDNA) we'll look at each 
#  substring from the smallest DNA of that length and compare it to all other DNA strings until
#  we don't find a match. When that happens, we look at all substrings of -1 the previous len,
#  and compare to all others... repeat this until we are able to find one that matches all DNA

# Let's find the smallest DNA, then remove that sequence from the dictionary
smallest_key, smallest_sequence = fasta_dict.popitem()
fasta_dict[smallest_key] = smallest_sequence
for key, sequence in fasta_dict.items():
    if len(smallest_sequence) > len(sequence):
        smallest_sequence = sequence
        smallest_key = key
fasta_dict.pop(smallest_key)

# Returns all substrings in a sequence s of len l (l must be >= len(s))
def all_substrings(s, l):
    if len(s) < l:
        print("Error: 'l' must be <= len(s)")
        return []
    num_sub_strings = len(s) - l + 1
    sub_strings = []
    for i in range(0,num_sub_strings):
        sub_strings.append(s[i:i+l])
    return sub_strings

# Go through each len (decresing) of the smallest_sequence and check all the substrings against
#  all other sequences
longest_substring = ''
longest_substring_found = False
match = True
for i in range(len(smallest_sequence), 0, -1):
    substrings = all_substrings(smallest_sequence,i)
    for substring in substrings:
        for value in fasta_dict.values():
            if substring not in value:
                match = False
                break
        if match:
            longest_substring_found = True
            longest_substring = substring
            break
            # We've found the substring, so we leave all loops
        else:
            match = True
            # Continue looking with this group of substrings (or move onto -1 len substrings)
    if longest_substring_found:
        break

print(longest_substring)

