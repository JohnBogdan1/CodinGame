import sys, math, numpy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L = int(raw_input())
H = int(raw_input())
T = raw_input()

#T = T.upper()

AlfHum="ABCDEFGHIJKLMNOPQRSTUVWXYZ?"

chars = {}

N = len(T)

nalf = len(AlfHum)


for i in xrange(H):
    
    ROW = raw_input()
    chars.setdefault(ord('?'), list()).append(ROW[26*L:26*L+L]) 
    for j in range(26):
        chars.setdefault(ord('A') + j, list()).append(ROW[j*L:j*L+L]) 
matrix = []
output = ""
for i in xrange(H):
    for char in T:
        char=char.upper()
        if char >= 'a' and char <= 'z':
            char += ('A' - 'a')
        elif char < 'A' or char > 'Z':
            char = '?'
        output += (chars[ord(char)])[i]
    output += "\n"

print output
    
        
    
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
