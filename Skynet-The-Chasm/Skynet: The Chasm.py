import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(raw_input()) # the length of the road before the gap.
gap = int(raw_input()) # the length of the gap.
platform = int(raw_input()) # the length of the landing platform.

# game loop
while 1:
    speed = int(raw_input()) # the motorbike's speed.
    coordX = int(raw_input()) # the position on the road of the motorbike.
    action = "WAIT"
    if speed < gap + 1:
        action = "SPEED"
    elif speed > gap + 1:
        action = "SLOW"
    if coordX == road - 1:
        action = "JUMP"
    if coordX > road + gap - 1:
        action = "SLOW"
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    print action # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
