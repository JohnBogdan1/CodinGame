import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
spaces = 0
newline = True

def print_newline():
    
    sys.stdout.write('\n')
    
    global newline
    
    newline = True

def print_char(char):
    
    global newline
    
    if newline == True:
        sys.stdout.write(spaces * ' ')
        newline = False
    sys.stdout.write(char)

def parse_and_print(cgxline):
    
    reading_string = False
    global spaces
    
    for c in cgxline:
        if reading_string == True:
            print_char(c)
            if c == '\'':
                reading_string = False
        else:
            if c == ' ':
                pass
            elif c == '\t':
                pass
            elif c == '(':
                if not newline:
                    print_newline()
                print_char(c)
                print_newline()
                spaces += 4
            elif c == ')':
                if not newline:
                    print_newline()
                spaces -= 4
                print_char(c)
                
            elif c == '\'':
                reading_string = True
                print_char(c)
                
            elif c == ';':
                print_char(c)
                if not newline:
                    print_newline()
            else:
                print_char(c)
            
    
n = int(raw_input())

for i in xrange(n):
    cgxline = raw_input()
    
    parse_and_print(cgxline)
