import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

 # N: the total number of nodes in the level, including the gateways
 # L: the number of links
 # E: the number of exit gateways
N, L, E = [int(i) for i in raw_input().split()]
links = []
for i in xrange(L):
     # N1: N1 and N2 defines a link between these nodes
    N1, N2 = [int(j) for j in raw_input().split()]
    links.append([N1, N2])
print >> sys.stderr, links
saves = []
for i in xrange(E):
    EI = int(raw_input()) # the index of a gateway node
    saves.append(EI)
# game loop
print >> sys.stderr, saves
def to_sever(x, y):
    sever_links = []
    if x in saves:
        sever_links.append([y, x])
    elif y in saves:
        sever_links.append([x, y])
    else:
        sever_links = []
    return sever_links

legaturi = []
for items in links:
    if to_sever(items[0], items[1]) != []:
        legaturi.extend(to_sever(items[0], items[1]))

print >> sys.stderr, legaturi
while 1:
    SI = int(raw_input()) # The index of the node on which the Skynet agent is positioned this turn
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    index = None
    print >> sys.stderr, "LEGATURI"
    
    print >> sys.stderr, legaturi
    for node in legaturi:
        if node[0] == SI:
            index = legaturi.index(node)
            break
    print >> sys.stderr, "INDEX"
    print >> sys.stderr, index
    if index != None:
        link = legaturi.pop(index)
    else:
        link = legaturi.pop()
    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print link[0], link[1]
