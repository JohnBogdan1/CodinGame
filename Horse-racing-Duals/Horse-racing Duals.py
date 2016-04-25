import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input())

lista = []
for i in xrange(N):
    Pi = int(raw_input())
    lista.append(Pi)

lista.sort()

min_diff = lista[1] - lista[0]

for i in range(1, len(lista) - 1):
        x = lista[i]
        y = lista[i + 1]
        if abs(y - x) < min_diff:
            min_diff = abs(y - x)
print min_diff
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
