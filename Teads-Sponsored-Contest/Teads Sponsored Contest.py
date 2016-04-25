import sys, math, numpy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input()) # the number of adjacency relations
graph = {}
for i in xrange(n):
     # xi: the ID of a person which is adjacent to yi
     # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in raw_input().split()]
    graph.setdefault(xi,list()).append(yi)
    graph.setdefault(yi,list()).append(xi)
    
#print >> sys.stderr, graph
count = 0

# Find a leaf
for vertice in graph.values():
    if len(vertice) == 1:
        leaf_vertix = graph.keys()[count]
        break
    count += 1

def find_path(graph, start):
    tuple = [start, start, 0]
    stack = []
    stack.append(tuple)
    max_dist = 0
    while len(stack) != 0:
        
        nextV = stack[len(stack)-1][0]
        parent = stack[len(stack)-1][1]
        distance = stack[len(stack)-1][2]
        
        #print >> sys.stderr, stack
        stack.pop()
        #print >> sys.stderr, stack
        if distance > max_dist:
            max_dist = distance
        #print >> sys.stderr, "nextV", nextV
        #print >> sys.stderr, "parent", parent
        for node in graph[nextV]:
            #print >> sys.stderr, graph[nextV]
            if node != parent:
                #stack = []
                stack.append([node, nextV, distance + 1])
                
                
    
    return max_dist+1



distanta = find_path(graph, leaf_vertix)
print (distanta)/2


