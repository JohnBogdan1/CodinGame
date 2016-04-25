import sys
import math
from random import randint
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

opponent_count = int(raw_input()) # Opponent count

x = None
y = None

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def adding_direction(harta):
    ll = Point(x,y)
    ur = Point(x,y)
    best_ll = Point(0, 0)
    best_ur = Point(-1, -1)
    
    for a in range(35):
        for b in range(20):
            ll = Point(a, b)
            ur = grow_ones(harta, ll)
            if area(ll, ur) > area(best_ll, best_ur): 
                best_ll = ll
                best_ur = ur
    
    result = [[best_ll.x, best_ll.y], [best_ur.x, best_ur.y]]
    
    return result
    
def grow_ones(harta, ll):
    ur = Point(ll.x - 1, ll.y - 1)
    x_max = 35
    y = ll.y - 1
    
    while y + 1 < 20 and harta[y + 1][ll.x] == 1:
        y = y + 1
        x = ll.x
        while x + 1 < x_max and harta[y][x + 1] == 1:
            x = x + 1
        x_max = x
        if area(ll, Point(x, y)) > area(ll, ur):
            ur = Point(x, y)
    return ur
   
def area(ll, ur):
    if ll.x > ur.x or ll.y > ur.y:
        return 0
    else:
        return (ur.x - ll.x + 1) * (ur.y - ll.y + 1)

def all_ones(harta, ll, ur):
    
    for x in range(ll.x, ur.x + 1):
        for y in range(ll.y, ur.y + 1):
            if harta[y][x] != 1 and harta[y][x] != 7:
                return False
    
    return True
    
first_choice = True

while 1:
    
    game_round = int(raw_input())
     # x: Your x position
     # y: Your y position
     # back_in_time_left: Remaining back in time
    x, y, back_in_time_left = [int(i) for i in raw_input().split()]
    
    
    oponnents = []
    for i in xrange(opponent_count):
         # opponent_x: X position of the opponent
         # opponent_y: Y position of the opponent
         # opponent_back_in_time_left: Remaining back in time of the opponent
        opponent_x, opponent_y, opponent_back_in_time_left = [int(j) for j in raw_input().split()]
        oponnents.append([opponent_x, opponent_y])
        
        
    grid = []
    for i in xrange(20):
        line = raw_input() # One line of the map ('.' = free, '0' = you, otherwise the id of the opponent)
        grid.append(line)
    
    #neutral choice
    tabel = []
    for item in grid:
        stoc = []
        for i in item:
            if i == '.':
                c = 1
            elif i == '0':
                c = 7
            else:
                c = 0
            
            stoc.append(c)
        tabel.append(stoc)
    
    
    if first_choice == True:
        choice = adding_direction(tabel)
        my_x_choice = choice[1][0]
        my_y_choice = choice[1][1]
        my_initial_x = choice[0][0]
        my_initial_y = choice[0][1]
        print >> sys.stderr, choice
    
    if all_ones(tabel, Point(my_initial_x, my_initial_y), Point(my_x_choice, my_y_choice)) == False:
        choice = adding_direction(tabel)
        my_x_choice = choice[1][0]
        my_y_choice = choice[1][1]
        my_initial_x = choice[0][0]
        my_initial_y = choice[0][1]
        print >> sys.stderr, choice
    
    
    first_choice = False
    check = False
    
    if x == my_x_choice and y == my_y_choice:
        my_x_choice = my_initial_x
        my_y_choice = my_initial_y
        check = True
        
    if x == my_initial_x and y == my_initial_y and check == True:
        first_choice = True
    elif all_ones(tabel, Point(my_initial_x, my_initial_y), Point(my_x_choice, my_y_choice)) == True and x == my_initial_x and y == my_initial_y:
        my_x_choice = choice[1][0]
        my_y_choice = choice[1][1]
        
    print my_x_choice, my_y_choice
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    # action: "x y" to move or "BACK rounds" to go back in time
