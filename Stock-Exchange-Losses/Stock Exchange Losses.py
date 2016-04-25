import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())
vs = raw_input().split()

max_loss = 0
current = 0

for i in range(n):
    if int(vs[i]) > current:
        current = int(vs[i])  
    loss = int(vs[i]) - current
    if loss < max_loss:
        max_loss = loss


print max_loss


# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
