import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
 
n = int(raw_input()) # the number of relationships of influence
graph = {}
for i in xrange(n):
     # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in raw_input().split()]
    graph.setdefault(str(x), list()).append(str(y))
    
#print >> sys.stderr, graph
def find_longest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        longest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_longest_path(graph, node, end, path)
                if newpath:
                    if not longest or len(newpath) > len(longest):
                        longest = newpath
        return longest
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

# The number of people involved in the longest succession of influences
lista = []

for i in graph.keys():
    lista.append(i)
for i in graph.values():
    for j in i:
        lista.append(j)

lista = list(set(lista))
#print >> sys.stderr, lista

output = []
for i in range(len(lista)):
    for j in range(len(lista)):
        if i != j:
            a = lista[i]
            b = lista[j]
            #print >> sys.stderr, a, b
            if find_longest_path(graph, a, b) != None:
                output.append(find_longest_path(graph, a, b))
#print >> sys.stderr, output
numbers = []
for item in output:
    numbers.append(len(item))

print max(numbers)
