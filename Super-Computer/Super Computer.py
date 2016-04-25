import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())
list = []
for i in xrange(n):
    j, d = [int(j) for j in raw_input().split()]
    list.append([j + d - 1, j])
times = 0

list.sort()

comps = [list[0]]
i = 1

while i < len(list):
    
    if list[i][1] > comps[len(comps) - 1][0]:
        comps.append(list[i])
    i+=1

print len(comps)
