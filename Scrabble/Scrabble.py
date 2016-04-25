import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
cuvinte = []
N = int(raw_input())

my_dict = {
    ('e', 'a', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u'): 1, 
    ('d', 'g'): 2,
    ('b', 'c', 'm', 'p'): 3,
    ('f', 'h', 'v', 'w', 'y'):4,
    'k':5,
    ('j', 'x'):8,
    ('q', 'z'):10
    }
for i in xrange(N):
    W = raw_input()
    if len(W) <= 7:
        cuvinte.append(W)

LETTERS = raw_input()

#print >> sys.stderr, cuvinte

cuvinte_pos = []
print >> sys.stderr, LETTERS
    
for cuv in cuvinte:
    ok = 1
    cuvant = list(cuv)
    litere = LETTERS
    #print >> sys.stderr, cuvant
    for l in cuvant:
        if l in litere:
            litere = litere.replace(l,'0',1)
            #print >> sys.stderr, litere
            ok = 0
        else:
            ok=1
            break
    if ok==0:
        cuvinte_pos.append(cuv)
    
print >> sys.stderr, cuvinte_pos
sume = []

for cuv in cuvinte_pos:
    suma = 0
    temp = list(LETTERS)
    word = list(cuv)
    x = len(word)
    y = len(temp)
    for i in range(x):
        if word[i] in temp:
            del(temp[temp.index(word[i])])
            item = next(v for k, v in my_dict.items() if word[i] in k)
            suma += item
        
    sume.append(suma)
    

maximus = max(sume)
index = sume.index(maximus)

cuvant = cuvinte_pos[index]
print cuvant

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
