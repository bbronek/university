import sys
set = set()

for line in sys.stdin:
    line = line.rstrip('\n')
    if line == "KONIEC KOLEKCJI":
        break
    set.add(line)

for line in sys.stdin:
    line = line.rstrip('\n')
    if line in set:
        print("TAK")
    else:
        print("NIE")
