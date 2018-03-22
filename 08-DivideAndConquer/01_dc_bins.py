"""
http://rosalind.info/problems/bins/
Binary search is the ultimate divide-and-conquer algorithm. To find a key k in a large file containing keys A[1..n] in sorted order, we first compare k with A[n/2], and depending on the result we recurse either on the first half of the file, A[1..n/2], or on the second half, A[n/2+1..n]. The recurrence now is T(n)=T(n/2)+O(1). Plugging into the master theorem (with a=1,b=2,d=0) we get the familiar solution: a running time of just O(logn).

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.[http://rosalind.info/glossary/algo-algorithms-by-dasgupta-papadimitriou-vazirani-mcgraw-hill-2006/]

Problem
The problem is to find a given set of keys in a given array.

Given: Two positive integers n≤105 and m≤105, a sorted array A[1..n] of integers from −105 to 105 and a list of m integers −105≤k1,k2,…,km≤105.

Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.

Sample Dataset
5
6
10 20 30 40 50
40 10 35 15 40 20
Sample Output
4 1 -1 -1 4 2
"""

# Building file name
probnum = 'bins'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

data_input = open(filename, 'r')
in_file = [x.replace('\n','') for x in data_input.readlines()]
n = int(in_file[0])
m = int(in_file[1])
n_sorted_list = [int(x) for x in in_file[2].split()]
m_queries = [int(x) for x in in_file[3].split()]

from math import ceil

# find the query using binary search
def bin_search(n_sorted, query, left=0, right=None):
    if right is None:
        right = len(n_sorted)-1

    # sanity check
    if right >= left:
        #middle = int(left + (right-left)/2)
        middle = ceil(left + (right-left)/2)

        if n_sorted[middle] == query:
            return middle
        elif n_sorted[middle] > query: #look further down
            return bin_search(n_sorted, query, left, middle-1)
        else: # n_sorted[middle] < query: #look further up
            return bin_search(n_sorted, query, middle+1, right)
    
    else: # not found
        return -1

#for m_query in n_sorted_list:
for m_query in m_queries:
    index = bin_search(n_sorted_list, m_query)
    if index >= 0:
        index += 1
    print(index, end = ' ')
print()

