import sys
import math
import Queue

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L, H = [int(i) for i in raw_input().split()]
chars = ""
numbers = []

for i in range(20):
    numbers.append([])
for i in xrange(H):
    numeral = raw_input()
    for j in range(20):
        numbers[j].append(numeral[j*L:j*L+L])
        
lista = []

for item in numbers:
    lista.append("".join(item))

S1 = int(raw_input())
num1 = ""

for i in xrange(S1):
    num1Line = raw_input()
    num1 += num1Line
    
S2 = int(raw_input())
num2 = ""
for i in xrange(S2):
    num2Line = raw_input()
    num2 += num2Line

numbers = lista
#print >> sys.stderr, num1
#print >> sys.stderr, num2
#print >> sys.stderr, numbers
operation = raw_input()
#print >> sys.stderr, operation

valNum1 = 0
for i in range(len(num1)/(H*L)):
    for j in range(len(numbers) - 1):
        j += 1    
        if numbers[j] == num1[i*H*L:i*H*L + H * L]:
            valNum1 += j * pow(20,(len(num1)/(H*L)) - i - 1)
valNum2 = 0
for i in range(len(num2)/(H*L)):
    for j in range(len(numbers) - 1):
        j += 1
        if numbers[j] == num2[i*H*L:i*H*L + H * L]:
            valNum2 += j * pow(20,(len(num2)/(H*L)) - i - 1)

#print >> sys.stderr, valNum1
#print >> sys.stderr, valNum2
if operation == '+':
    result = valNum1 + valNum2
elif operation == '-':
    result = valNum1 - valNum2
elif operation == '*':
    result = valNum1 * valNum2
elif operation == '/':
    result = valNum1 / valNum2

#print >> sys.stderr,result

import Queue

queue = Queue.Queue()
#print >> sys.stderr, result
while result > 20:
    
    queue.put(result % 20)
    queue.put(result / 20)
    
    result /= 20

lista = []
while not queue.empty():
    x = queue.get()
    if x < 20:
        lista.append(x)
lista.reverse()
if not len(lista):
    for i in range(H):
        print numbers[result][i*L:i*L + L]
else:
    for item in lista:
        for i in range(H):
            print numbers[item][i*L:i*L + L]
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
