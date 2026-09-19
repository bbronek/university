import sys


def main():
    connections = {}
    while 1:
        line = input()
        if line == "END":
            break
        line = line.split(" -> ")
        source, destination = line[0], line[1]
        if source not in connections:
            connections[source] = []
        if destination not in connections:
            connections[destination] = []
        connections[source].append(destination)
    for line in sys.stdin:
        line = line.rstrip("\n")
        line = line.split(" ? ")
        source, destination = line[0], line[1]
        if destination in connections.get(source, []):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
