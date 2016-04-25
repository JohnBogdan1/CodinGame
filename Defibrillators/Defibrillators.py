import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

LON = raw_input()
LAT = raw_input()
LON = LON.replace(",", ".")
LAT = LAT.replace(",", ".")
LON = float(LON)
LAT = float(LAT)
N = int(raw_input())

minim = 1000
dictionar = {}
index = ""
for i in xrange(N):
    DEFIB = raw_input()
    a, b, c, d, e, f = DEFIB.split(";")
    if N == 1:
        print b
    else:
        dictionar[a] = [b, c, d, e , f] 
        e = e.replace(",", ".")
        f = f.replace(",", ".")
        lon = float(e)
        lat = float(f)
    
        x = (lon - LON) * math.cos((lat + LAT)/2)
        y = (lat - LAT)
        d = math.sqrt(x ** 2 + y ** 2) * 6371
        if d < minim:
            minim = d
            index = a

print dictionar[index][0]
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
