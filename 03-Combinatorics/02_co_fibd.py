"""
http://rosalind.info/problems/fibd/
Wabbit Season
Problem

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100n≤100 and m≤20m≤20.

Return: The total number of pairs of rabbits that will remain after the nn-th month if all rabbits live for mm months.
"""

# Building file name
probnum = 'fibd'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

# Parse out the variables from the file
data_input = open(filename, 'r')
in_file = data_input.readline().replace('\n','').split()

n = int(in_file[0]) # number of months to run sim
m = int(in_file[1]) # each rabbit pair lives on for m-years
k = 1 # each pair produces 1 pair of immature rabbits
initial = 1 # start with 1 pair of immature rabbits

fib_gen = []
i = 0
while i < n:
    if i < 2:
        fib_gen.append(1)
    elif i < m:
        fib_gen.append((fib_gen[i-2]*k) + fib_gen[i-1])
    elif i <= m+1:
        fib_gen.append((fib_gen[i-2]*k) + fib_gen[i-1] - 1)
    else:
        fib_gen.append((fib_gen[i-2]*k) + fib_gen[i-1] - fib_gen[i-m-1])
    i += 1

print(fib_gen)
print(fib_gen[-1])

'''
n = 10
m = 3
# Works but is way too slow
pop = [] # population at first month
newborn = initial
matings = 0
for i in range(1,n+1):
    # remove dead
    print('#####Start month', i)
    #print('Start', pop)

    pop = [x+1 for x in pop]
    #print('After aged', pop)

    pop = [x for x in pop if x<m]
    #print('After deaths', pop)

    matings = len([x for x in pop if x>0])
    #print('How many new matings', matings)

    pop += [0]*newborn
    #print('After addition of newborn from previous season', pop)

    newborn = matings
    print('Pop', pop)
    #print('Total pop', len(pop))
    #print()


print('Final population ages:', pop)
print('Final population:', len(pop))
'''

