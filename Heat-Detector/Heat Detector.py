import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# W: width of the building.
# H: height of the building.
W, H = [int(i) for i in raw_input().split()]
N = int(raw_input()) # maximum number of turns before game over.
X0, Y0 = [int(i) for i in raw_input().split()]
#print >> sys.stderr, W
#print >> sys.stderr, H
W1 = 0
H1 = 0
X = X0
Y = Y0
# game loop
while 1:
    BOMB_DIR = raw_input() # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    for i in range(len(BOMB_DIR)):
        if BOMB_DIR[i] == "U":
            H = Y
        elif BOMB_DIR[i] == "D":
            H1 = Y
        elif BOMB_DIR[i] == "L":
            W = X
        elif BOMB_DIR[i] == "R":
            W1 = X
    
    
    X = (W - W1)/2 + W1
    Y = (H - H1)/2 + H1
   
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    print X, Y
    
    # the location of the next window Batman should jump to.
