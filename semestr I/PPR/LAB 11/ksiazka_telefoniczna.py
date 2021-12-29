import sys
d = {}

for line in sys.stdin:
    line = line.rstrip('\n')
    if line == "KONIEC":
        break
    v = line.split(',')
    d[v[0]] = v[1]


for line in sys.stdin:
    line = line.rstrip('\n')
    print(d[line])