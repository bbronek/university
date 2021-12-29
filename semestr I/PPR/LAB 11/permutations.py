from collections import Counter
import sys

for line in  sys.stdin:
    line = line.rstrip('\n').split()
    a,b= line[0],line[1]
    if(Counter(a)==Counter(b)):
        print("TAK")
    else:
        print("NIE")