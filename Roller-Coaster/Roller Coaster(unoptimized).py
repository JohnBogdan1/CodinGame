import sys
import math
from collections import deque
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
queue = deque([])
l, c, n = [int(i) for i in raw_input().split()]
for i in xrange(n):
    pi = int(raw_input())
    queue.append(pi)

print >> sys.stderr, queue, l, c, n

dirhams = 0
for i in xrange(c):
    suma = 0
    groups = deque([])
    for j in range(n):
        suma += queue[j]
        if suma > l:
            break
        dirhams += queue[j]
        groups.append(queue[j])
    for ppl in groups:
        queue.popleft()
        queue.append(ppl)

print dirhams
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
