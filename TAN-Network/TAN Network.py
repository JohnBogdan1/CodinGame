import sys
import math
import heapq
from collections import defaultdict, deque

routes = {}
start_point = raw_input().replace("StopArea:","")
end_point = raw_input().replace("StopArea:","")
n = int(raw_input())

asocieri = {}
for i in xrange(n):
    stop_name = raw_input().replace("StopArea:","").split(",")
    asocieri[stop_name[0]]=[stop_name[1], stop_name[3], stop_name[4]]
m = int(raw_input())

nodes = asocieri.keys()

for i in xrange(m):
    route = raw_input()
    
    sets = route.replace("StopArea:","").split()
    routes.setdefault(sets[0], list()).append(sets[1])

def decrease_key(Q, dist_values):
    for i in range(len(Q)):
        for j in range(len(Q)):
            if dist_values[Q[i][1]] < dist_values[Q[j][1]]:
                s = Q[i]
                Q[i] = Q[j]
                Q[j] = s

def dijkstra(pairs, distances, nodes, sursa, destinatie):
    Q = []
    selected = {}
    parent = {}
    dist_values = {}

    for nod in nodes:
        selected[nod] = False

    selected[sursa] = True

    heapq.heappush(Q, (0, sursa))

    for nod in nodes:
        if nod in pairs[sursa]:
            dist_values[nod] = distances[(sursa, nod)]
            heapq.heappush(Q, (dist_values[nod], nod))
            parent[nod] = sursa
        else:
            dist_values[nod] = float("inf")
            parent[nod] = None

    while Q:
        dist, u = heapq.heappop(Q)
        selected[u] = True

        if u in pairs:
            for nod in pairs[u]:
                if (not selected[nod]) and dist_values[nod] > dist_values[u] + distances[(u, nod)]:
                    dist_values[nod] = dist_values[u] + distances[(u, nod)]
                    parent[nod] = u
                    heapq.heappush(Q, (dist_values[nod], nod))
                    decrease_key(Q, dist_values)

    # reconstruct the path back to the source
    drum = deque()
    nod = parent[destinatie]

    drum.appendleft(destinatie)

    while nod != None:
        drum.appendleft(nod)
        nod = parent[nod]

    # return the path
    #print >> sys.stderr, "Path between %s si %s: %s" % (sursa, destinatie, list(drum))
    return list(drum)

if __name__ == '__main__':

    distances = {}
    for leaf in routes.items():
       
        for i in range(len(leaf[1])):
            
            longB = math.radians(float(asocieri[leaf[1][i]][2]))
            longA = math.radians(float(asocieri[leaf[0]][2]))
            
            latA =  math.radians(float(asocieri[leaf[1][i]][1]))
            latB =  math.radians(float(asocieri[leaf[0]][1]))
 
            x = (longB - longA) * math.cos(((latA + latB)) / 2)
            y = (latB - latA)
            d = math.sqrt(x ** 2 + y ** 2) * 6371
            distances[(leaf[0], leaf[1][i])] = d

    #print >> sys.stderr, "Nodes: ", nodes
    #print >> sys.stderr, "Routes data: ", routes
    #print >> sys.stderr, 'Distances data:', distances
    #print >> sys.stderr, start_point, end_point, "\n"

    result = dijkstra(routes, distances, nodes, start_point, end_point)
    
    if start_point in result and len(result) == 1:
        print asocieri[start_point][0].replace("\"", "")
    elif start_point not in result:
        print "IMPOSSIBLE"
    else:
        for id in result:
                print asocieri[id][0].replace("\"", "")
