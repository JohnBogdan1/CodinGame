import sys
import math
import binascii
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

MESSAGE = raw_input()

lista = []
lista_veche = []
pre=""

for item in MESSAGE:
    lista.append(item)


for item in lista:
    lungime = len(bin(int(binascii.hexlify(item), 16))[2:])
    binar = bin(int(binascii.hexlify(item), 16))[2:]
    print >> sys.stderr, binar
    if lungime < 7:
        pre = '0' + binar
        
        lista_veche.append(pre)
    else:
        lista_veche.append(binar)

lis = " ".join(lista_veche)
lista_noua = lis.replace(" ", "")

mesaj = ""

count1 = 0
count2 = 0


i = 0

while i < len(lista_noua):
    if lista_noua[i] == '1':
        j = i
        mesaj += "0 "
      
        while j < len(lista_noua) and lista_noua[j] != '0':
            count1 += 1
            j += 1
            
        i = j - 1
        
        mesaj += count1 * "0"
        mesaj += " "
    if lista_noua[i] == '0':
        j = i
        mesaj += "00 "
        while j < len(lista_noua) and lista_noua[j] != '1':
            j += 1
            count2 += 1
        i = j -1
        mesaj += count2 * "0"
        mesaj += " "
    i += 1
    count1 = 0
    count2 = 0

print mesaj.rstrip()

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
