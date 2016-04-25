# not ended

import sys
import math
from collections import defaultdict

routes = {}
start_point = raw_input().replace("StopArea:","")
end_point = raw_input().replace("StopArea:","")
n = int(raw_input())

asocieri = {}
for i in xrange(n):
    stop_name = raw_input().replace("StopArea:","").split(",")
    asocieri[stop_name[0]]=[stop_name[1], stop_name[3], stop_name[4]]
m = int(raw_input())

for i in xrange(m):
    route = raw_input()
    
    sets = route.replace("StopArea:","").split()
    routes.setdefault(sets[0], list()).append(sets[1])
    #routes.setdefault(sets[1], list()).append(sets[0])
#print >> sys.stderr, routes

#######################################
 
 
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        
        self.distance = sys.maxint
                
        self.visited = False  
        
        self.previous = None
 
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    
    """def __iter__(self):
        return iter([self.id])"""
        
    def get_connections(self):
        return self.adjacent.keys()  
 
    def get_id(self):
        return self.id
 
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
 
    def set_distance(self, dist):
        self.distance = dist
 
    def get_distance(self):
        return self.distance
 
    def set_previous(self, prev):
        self.previous = prev
 
    def set_visited(self):
        self.visited = True
 
    def __str__(self):
        return str([x.id for x in self.adjacent])
 
class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.weights = {}
        self.num_vertices = 0
 
    def __iter__(self):
        return iter(self.vert_dict.values())
 
    def cost(self, a, b):
        return self.weights[a][1]
        
    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        
        return new_vertex
 
    def get_vertex(self, n):
       
        for c in self.vert_dict.values():
            print c
        
        if n in self.vert_dict:
            return self.vert_dict[n]
            
        else:
            return None
 
    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
 
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
 
    def get_vertices(self):
        return self.vert_dict.keys()
 
    def set_previous(self, current):
        self.previous = current
 
    def get_previous(self, current):
        return self.previous
 

import heapq


class PriorityQueue:
    """ Wrapper sur heapq (utilisation simplifiee) """

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def dijkstra(graph, _start, _goal):
    frontier = PriorityQueue()
    frontier.put(_start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[_start] = None
    cost_so_far[_start] = 0
    
    while not frontier.empty():
        current = frontier.get()

        if current == _goal:
            break
        
        if current in graph.vert_dict.keys():
            for next in [graph.vert_dict[current]]:
    
                new_cost = cost_so_far[current] + graph.cost(current, next)
                
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    frontier.put(next, priority)
                    came_from[next] = current

    return came_from, cost_so_far


def reconstruct_path(_came_from, _start, _goal):
    current = _goal
    path = [current]
    while current != _start:
        current = _came_from[current]
        path.append(current)
    path.reverse()
    return path


if __name__ == '__main__':
 
    g = Graph()
    for point in routes.keys():
        g.add_vertex(point)
 
    for leaf in routes.items():
       
        for i in range(len(leaf[1])):
 
            x = (float(asocieri[leaf[1][i]][2]) - float(asocieri[leaf[0]][2])) * math.cos(((float(asocieri[leaf[1][i]][1]) + float(asocieri[leaf[0]][1])))/2)
            y = ((float(asocieri["".join(leaf[1][i])][1]) - float(asocieri[leaf[0]][1])))
            d = math.sqrt(x ** 2 + y ** 2) * 6371
            g.add_edge(leaf[0], leaf[1][i], d)
            
    #print >> sys.stderr, 'Graph data:'
    
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
           # print >> sys.stderr, '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))
            g.weights[vid] = [wid, v.get_weight(w)]
    #print g.get_vertex("ABLA")
    came_from, cost_so_far = dijkstra(g, start_point, end_point)
    print >> sys.stderr, "*******************MAIN***************************"
    
    # reconstructed the path and the cost associated
    #path = reconstruct_path(came_from, _start=start_point, _goal=end_point)
    #print >> sys.stderr, "path, cost: %s, %s" % (path, cost)

    #for id_Station in path:
       # print dict_stations[id_Station].full_name
    
    target = g.get_vertex(end_point)
    path = [target.get_id()]
   # shortest(target, path)
    #print 'The shortest path : %s' %(path[::-1])
    result = path[::-1]
    print >> sys.stderr, result
    if start_point == end_point:
        print asocieri[start_point].replace("\"", "")
       
    else:
       
        if result != []:
            for id in result:
                print asocieri[id][0].replace("\"", "")
        else:
            print "IMPOSSIBLE"
