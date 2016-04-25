import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while True:
    index = 0
    mt_max_height = -1 
    for i in xrange(8):
        mountain_h = int(raw_input())  # represents the height of one mountain, from 9 to 0.
        if mountain_h > mt_max_height:
            # i find the highest mountain and by the end of the turn i shoot it
            mt_max_height = mountain_h
            index = i
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    # The number of the mountain to fire on.
    print index
