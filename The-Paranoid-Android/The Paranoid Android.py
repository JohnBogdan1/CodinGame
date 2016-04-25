import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nbFloors: number of floors
# width: width of the area
# nbRounds: maximum number of rounds
# exitFloor: floor on which the exit is found
# exitPos: position of the exit on its floor
# nbTotalClones: number of generated clones
# nbAdditionalElevators: ignore (always zero)
# nbElevators: number of elevators
nbFloors, width, nbRounds, exitFloor, exitPos, nbTotalClones, nbAdditionalElevators, nbElevators = [int(i) for i in raw_input().split()]
elevators = {}
for i in xrange(nbElevators):
    # elevatorFloor: floor on which this elevator is found
    # elevatorPos: position of the elevator on its floor
    elevatorFloor, elevatorPos = [int(j) for j in raw_input().split()]
    print >> sys.stderr, elevatorFloor, elevatorPos
    elevators[elevatorFloor] = elevatorPos
elevators[exitFloor] = exitPos
print >> sys.stderr, elevators
# game loop
elevator_direction = ""
while 1:
    # cloneFloor: floor of the leading clone
    # clonePos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    cloneFloor, clonePos, direction = raw_input().split()
    cloneFloor = int(cloneFloor)
    clonePos = int(clonePos)
    print >> sys.stderr, clonePos, cloneFloor
    if cloneFloor == -1:
        print "WAIT"
    else:
        difference = clonePos - elevators[cloneFloor]
        print >> sys.stderr, difference
        if difference > 0:
            elevator_direction = "LEFT"
        elif difference < 0:
            elevator_direction = "RIGHT"
        else:
            elevator_direction = direction
        
        if direction != elevator_direction:
            print "BLOCK"
        else:
            print "WAIT"
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
