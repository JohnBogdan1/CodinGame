import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input())

puncteX = []
puncteY = []
for i in xrange(N):
    X, Y = [int(j) for j in raw_input().split()]
    puncteX.append(X)
    puncteY.append(Y)

puncteY.sort()
print >> sys.stderr, puncteY

if len(puncteY) % 2 == 1:
    median = puncteY[(len(puncteY) - 1)/2]
elif len(puncteY) % 2 == 0:
    median = (puncteY[(len(puncteY))/2 - 1] + puncteY[len(puncteY)/2]) / 2

mainCableX = max(puncteX) - min(puncteX)

distance = mainCableX

for item in puncteY:
    distance += abs(median - item)
print >> sys.stderr, median
print >> sys.stderr, mainCableX

print distance
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
