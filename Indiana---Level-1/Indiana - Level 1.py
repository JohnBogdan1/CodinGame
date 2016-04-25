import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

 # W: number of columns.
 # H: number of rows.
W, H = [int(i) for i in raw_input().split()]
lista = []
for i in xrange(H):
    LINE = raw_input().split() # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    lista.append(LINE)
EX = int(raw_input()) # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

#print >> sys.stderr, lista
while 1:
    XI, YI, POS = raw_input().split()
    XI = int(XI)
    YI = int(YI)
    digit = lista[YI][XI]
    print >> sys.stderr, digit
    if digit in ['1', '3', '7', '8', '9', '12', '13']:
        YI += 1
    elif digit in ['2', '6']:
        if POS == "LEFT":
            XI += 1
        else:
            XI -= 1
    elif digit in ['4']:
        if POS == "TOP":
            XI -= 1
        elif POS == "RIGHT":
            YI += 1
    elif digit in ['5']:
        if POS == "TOP":
            XI += 1
        elif POS == "LEFT":
            YI += 1
    elif digit in ['10']:
        XI -= 1
    elif digit in ['11']:
        XI += 1
    print XI, YI
    i += 1
