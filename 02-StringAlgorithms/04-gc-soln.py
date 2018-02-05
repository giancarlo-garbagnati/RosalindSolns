"""
Identifying Unknown DNA Quickly
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
Sample Output
Rosalind_0808
60.919540
"""

# Building file name
probnum = 'gc'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.fasta'

# Parse out the variables from the file
data_input = open(filename, 'r')
fasta_file = [x.replace('\n','') for x in data_input.readlines()]

# Function to determine GC of a DNA seq
def gc_content(dna_s):
    total = 0
    gc = 0
    for nt in dna_s:
        total += 1
        if nt.upper() in ['G','C']:
            gc += 1
    return gc/total

# Sort the fasta file into a dictionary with key being labelling info, and value as a tuple with (sequence, gc content)
fasta_dict = dict()
i = 0
key = ''
seq = ''
highest_gc = 0
highest_key = ''
for i in range(0,len(fasta_file)):
    line = fasta_file[i]
    # if it starts with a '>', it's a label, and so we use it as the key for the following sequence
    if line[0] == '>':
        key = line[1:]
    # otherwise we build the dna sequence
    else:
        seq += line

        # if the next line is another label or we've reached the end of the list, we update gc/highestgc/etc and reset seq
        if (i+1 >= len(fasta_file)) or (fasta_file[i+1][0] == '>'):
            gc = gc_content(seq)*100
            fasta_dict[key] = (seq, gc)

            # Check to see if this gc is higher than the previous highest
            if gc > highest_gc:
                highest_gc = gc
                highest_key = key

            # Reset current_seq for next sequence
            seq = ''

print(highest_key)
print(fasta_dict[highest_key][1])
