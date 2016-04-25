import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

R = int(raw_input())
L = int(raw_input())

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
def lookAndSay(number):
    #if number is string, i take every number from string and convert it to int
    #numbers(even digits) are added to vector
    if type(number) == str:
        vector = []
        car = []
        
        for item in number.split():
            car.append(int(item))
        
        for item in car:
            vector.append(item)
        vector.append(0)
    else:
        vector = [number, 0]
    
    times = 1
    first = vector[0]
    num = vector[1:]
    sir = ""
    
    for actual in num:
        if actual != first:
            sir += str(times) + " " + str(first)
            sir += " "
            times = 1
            first = actual
        else:
            times += 1
    return sir

numar = R
lista = []
if L == 1:
    print numar
else:
    for i in range(L-1):
        numar = lookAndSay(numar)
        lista.append(numar)
    print lista[L-2].strip()
