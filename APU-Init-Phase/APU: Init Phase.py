import sys, math

# Don't let the machines win. You are humanity's last hope...

width = int(raw_input()) # the number of cells on the X axis
height = int(raw_input()) # the number of cells on the Y axis

lines = []
for i in xrange(height):
    line = raw_input() # width characters, each either 0 or .
    lines.append(line)


while 1:
    curr_posX = 0
    curr_posY = 0
    found = False
    for i in range(height):
        for j in range(len(lines[i])):
            if lines[i][j] == '0':
                curr_posX = j
                curr_posY = i
                found = True
                break
        if found:
            break
    
    right_posX = curr_posX
    right_posY = curr_posY
    exists1 = False
    
    for i in range(right_posX + 1, width):
        if lines[curr_posY][i] == '0':
            right_posX = i
            exists1 = True
            break
    if not exists1:
        right_posX = -1
        right_posY = -1
    
    bottom_posX = curr_posX
    bottom_posY = curr_posY
    exists2 = False
        
    for i in range(bottom_posY + 1, height):
        if lines[i][curr_posX] == '0':
            bottom_posY = i
            exists2 = True
            break
        
    if not exists2:
        bottom_posX = -1
        bottom_posY = -1
    
    print curr_posX, curr_posY, right_posX, right_posY, bottom_posX, bottom_posY
    
    lines[curr_posY] = lines[curr_posY].replace("0",",", 1)
    
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
 # Three coordinates: a node, its right neighbor, its bottom neighbor
