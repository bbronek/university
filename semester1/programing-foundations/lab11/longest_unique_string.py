import sys
d = {}
v = []
for line in sys.stdin:
    line = line.rstrip('\n')
    if line in d:
        d[line] += 1
    else:
        d[line] = 1
for key in d:
    if(d[key] ==1):
        v.append(key)
v.sort(key=len)
print(v[-1])
