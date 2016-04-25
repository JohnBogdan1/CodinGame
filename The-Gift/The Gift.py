import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input())
C = int(raw_input())

bugete = []
for i in xrange(N):
    B = int(raw_input())
    bugete.append(B)
bugete.sort()
#print >> sys.stderr, bugete

if sum(bugete) < C:
    print "IMPOSSIBLE"
else:

    contributions = []
    people_left = len(bugete)
    cost = C
    for buget in bugete:
        average = cost / people_left
        contribution = buget if average > buget else average
        people_left -= 1
        cost -= contribution
        contributions.append(contribution)
    #print >> sys.stderr, contributions
    for banut in contributions:
        print banut


# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
