import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(raw_input())
h = int(raw_input())

def search(map, x, y):
    
    visit_map = [ [False] * l for i in range(h) ]

    list = [[x, y]]

    surface = 0
    
    while len(list) != 0:
        cell = list[len(list) - 1]
        list.pop()
        
        if visit_map[cell[1]][cell[0]] == False:
            visit_map[cell[1]][cell[0]] = True
            
            
            if map[cell[1]][cell[0]] == 'O':
                surface += 1
                
                if cell[0] > 0:
                    if visit_map[cell[1]][cell[0] - 1] == False and map[cell[1]][cell[0] - 1] == 'O':
                        list.append([cell[0] - 1, cell[1]])
                if cell[0] < l - 1:
                    if visit_map[cell[1]][cell[0] + 1] == False and map[cell[1]][cell[0] + 1] == 'O':
                        list.append([cell[0] + 1, cell[1]])
                if cell[1] > 0:
                    if visit_map[cell[1] - 1][cell[0]] == False and map[cell[1] - 1][cell[0]] == 'O':
                        list.append([cell[0], cell[1] - 1])
                if cell[1] < h - 1:
                    if visit_map[cell[1] + 1][cell[0]] == False and map[cell[1] + 1][cell[0]] == 'O':
                        list.append([cell[0], cell[1] + 1])
                    
    return surface

map = []
for i in xrange(h):
    row = raw_input()
    map.append(row)

n = int(raw_input())
for i in xrange(n):
    x, y = [int(j) for j in raw_input().split()]
    print search(map, x, y)
