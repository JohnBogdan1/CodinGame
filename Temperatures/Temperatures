import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input()) # the number of temperatures to analyse
TEMPS = raw_input() # the N temperatures expressed as integers ranging from -273 to 5526


        
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
lista = []
result = 0
temperature = ''
TEMPS += ' '
if N == 0:
        print 0
else:
    for i in TEMPS:
            if i != " ":
                temperature += i
            else:
                temperature = int(temperature)
                lista.append(temperature)
                if result == 0:
                    result = temperature
    
                abs_temperature = abs(temperature)
    
                if abs_temperature <= abs(result) and abs_temperature != 0:
                    result = temperature
                temperature = ''
    
    for item in lista:
        if abs(result) == item:
            result = item
    print result
