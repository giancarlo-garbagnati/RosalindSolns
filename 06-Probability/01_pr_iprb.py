"""
http://rosalind.info/problems/iprb/
Introduction to Mendelian Inheritance
Problem

Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X represent the random variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X=red)=35 and Pr(X=blue)=25.

Random variables can be combined to yield new random variables. Returning to the ball example, let Y model the color of a second ball drawn from the bag (without replacing the first ball). The probability of Y being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents all possible individual probabilities for X and Y, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree; see Figure 2 for an illustrative example.

An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or 310+110=25 (see Figure 2 above).

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Sample Dataset
2 2 2
Sample Output
0.78333
"""

# Building file name
probnum = 'iprb'
filename = '../data/rosalind_' + probnum + '.txt'
#filename = '../data/rosalind_' + probnum + '_sample.txt'

data_input = open(filename, 'r')
in_file = [x.replace('\n','') for x in data_input.readlines()]

inputs = [int(x) for x in in_file[0].split()]

# homozygous dominant
k = inputs[0]
# heterozygous
m = inputs[1]
# homozygous recessive
n = inputs[2]

pop = k+m+n

# three factors to multiply: picking first individual * picking second individual * probability of a dominant gene
# combinations that could give a dominant gene:
# > dom x dom -> 100%
# > dom x hetero -> 100%
# > dom x recessive -> 100%
# > hetero x dom -> 100%
# > hetero x hetero -> 75%
# > hetero x recessive -> 50%
# > recessive x dom -> 100%
# > recessive x hetero -> 50%
# > recessive x recessive -> 0%

# we'll calculate the prob of recessive, and get the dom probability from that
# hetero x hetero
hxh_1st = m/pop
hxh_2nd = (m-1)/(pop-1)
hxh_pR = 0.25
hxh = hxh_1st * hxh_2nd * hxh_pR
# hetero x recessive
hxr_1st = m/pop
hxr_2nd = n/(pop-1)
hxr_pR = 0.5
hxr = hxr_1st * hxr_2nd * hxr_pR
# recessive x hetero
rxh_1st = n/pop
rxh_2nd = m/(pop-1)
rxh_pR = 0.5
rxh = rxh_1st * rxh_2nd * rxh_pR
# recessive x recessive
rxr_1st = n/pop
rxr_2nd = (n-1)/(pop-1)
rxr_pR = 1
rxr = rxr_1st * rxr_2nd * rxr_pR

prob_two_recessive = hxh + hxr + rxh + rxr
prob_dominant = 1-prob_two_recessive

print(prob_dominant)
