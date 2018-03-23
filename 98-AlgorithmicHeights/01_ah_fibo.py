"""
http://rosalind.info/problems/fibo/
Fibonacci numbers
Problem
The Fibonacci numbers 0,1,1,2,3,5,8,13,21,34,… are generated by the following simple rule
Fn=⎧⎩⎨⎪⎪Fn−1+Fn−2,1,0,n>1,n=1,n=0.

Given: A positive integer n≤25.

Return: The value of Fn.

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.[http://rosalind.info/glossary/algo-algorithms-by-dasgupta-papadimitriou-vazirani-mcgraw-hill-2006/]
"""

# Building file name
probnum = 'fibo'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

data_input = open(filename, 'r')
in_file = [x.replace('\n','') for x in data_input.readlines()]
n = int(in_file[0])

fibo_list = [0,1]

if n >= len(fibo_list):
    for i in range(2,n+1):
        next_fibo_element = fibo_list[i-2] + fibo_list[i-1]
        fibo_list.append(next_fibo_element)

print(fibo_list[n])