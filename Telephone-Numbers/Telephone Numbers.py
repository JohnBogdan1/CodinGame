import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input())
lista = []
for i in xrange(N):
    telephone = raw_input()
    lista.append(telephone)
    #print >> sys.stderr, telephone
    
print >> sys.stderr, lista

if N == 1:
    print len(telephone)
else:
    lista_noua = []
    k = 0
    for i in range(N-1):
        current = lista[k]
        nexxt = lista[i+1]
        print >> sys.stderr, current, nexxt
        if len(current) == len(nexxt):
            if current[0] == nexxt[0]:
                for j in range(1, len(current)-1):
                    if current[j] != nexxt[j]:
                        lista_noua.append(current[j])
                        lista_noua.append(nexxt[j])
            else:
                lista_noua.append(current)
                lista_noua.append(nexxt)
                print len("".join(lista_noua))
                break
            print len("".join(lista_noua))
        elif len(current) > len(nexxt):
            if nexxt in current and current.startswith(nexxt):
                lista_noua.append(current)
                print len("".join(lista_noua))
            
    
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

# The number of elements (referencing a number) stored in the structure.

