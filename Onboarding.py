import sys, math

# CodinGame planet is being attacked by slimy insectoid aliens.
# <---
# Hint:To protect the planet, you can implement the pseudo-code provided in the statement, below the player.

# game loop
while 1:
    enemy1 = raw_input() # name of enemy 1
    dist1 = int(raw_input()) # distance to enemy 1
    enemy2 = raw_input() # name of enemy 2
    dist2 = int(raw_input()) # distance to enemy 2
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    # if an enemy is closer than the other, shoot the closest one
    if dist1 < dist2:
        print enemy1
    else:
        print enemy2
    #print "name of the enemy" # You have to output a correct ship name to shoot ("Buzz", enemy1, enemy2, ...)
