import sys
from itertools import permutations
for n in sys.stdin:
    n = n.rstrip('\n')
    n = sorted(n)
    for p in permutations(n):
        print(''.join(p))