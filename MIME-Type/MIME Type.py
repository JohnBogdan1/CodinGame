import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input()) # Number of elements which make up the association table.
Q = int(raw_input()) # Number Q of file names to be analyzed.
dictionar = {}

for i in xrange(N):
    # EXT: file extension
    # MT: MIME type.
    EXT, MT = raw_input().split()
    dictionar[EXT.lower()] = MT

print >> sys.stderr, dictionar
lista = []

unknown = "UNKNOWN"
for i in xrange(Q):
    FNAME = raw_input() # One file name per line.
    
    FNAME = FNAME.lower()
    print >> sys.stderr, FNAME
    pos = FNAME.rfind(".")
    if pos == -1:
        print unknown
    else:
        FNAME = FNAME[pos+1:]
        #print >> sys.stderr, FNAME
        index = dictionar.__contains__(FNAME)
        if index:
            print dictionar[FNAME]
        else:
            print unknown
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
