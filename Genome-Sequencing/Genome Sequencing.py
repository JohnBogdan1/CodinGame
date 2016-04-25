import sys
import math
import itertools

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# EASIER VERSION: DYNAMIC PROGRAMMING!

n = int(raw_input())
order = []
adn_seq = []

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
permutations = []



for i in xrange(n):
    subseq = raw_input()
    adn_seq.append(subseq)
    order.append(i)


for i in itertools.permutations(order):
    permutations.append(i)

print >> sys.stderr, permutations
print >> sys.stderr, adn_seq

def factorial(num):
    p = num
    while num != 1:
        num = num - 1
        p = p * num
    return p
    
number = factorial(n)

bestword = ""
for j in range(number):
    
    perm = permutations[j]
    match = False
    lastword = adn_seq[perm[0]]
    #print >> sys.stderr, lastword
    
    
    for i in range(1, len(adn_seq)):
        
        match = False
        first = lastword
        second = adn_seq[perm[i]]
        #print >> sys.stderr, first
        for k in range(len(first)):
            #print >> sys.stderr,k
            if len(second) >= len(first) - k:
                if first[k:] == second[0:len(first)-len(first[:k])]:
                    match = True
                if match == True:
                    lastword = first + second[len(first) - k:]
                    #print >> sys.stderr, lastword
                    break
            else:
                if first[k : k + len(second)] == second[0 : len(first) - len(first[k:k+len(second)])]:
                    match = True
                if match == True:
                    
                    lastword = first
                    #print >> sys.stderr, lastword
                    break
        if match == False:
            
            lastword = first + second
    
    if len(bestword) == 0 or len(lastword) < len(bestword):
        bestword = lastword
            
print >> sys.stderr, bestword         
print len(bestword)
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
