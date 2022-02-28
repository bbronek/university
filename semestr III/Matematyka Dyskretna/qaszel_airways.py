# Bartosz Bronikowski 
# Qaszel Airways 13.01.2022

class Vertex:
    def __init__(self, n):
        self.name = n 
        self.neighbours = list()

    def add_neighbour(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()

    def remove_neighbour(self, v):
        if v in self.neighbours:
            self.neighbours.remove(v)
    
    def connection_existance(self, v):
        if v in self.neighbours:
            print("TAK")
        else:
            print("NIE")
    
    def number_of_connections(self):
        print(len(self.neighbours))

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v):
        new_vertex = Vertex(v)
        self.vertices[v] = new_vertex
    
    def add_edge(self, f, t):
        if f not in self.vertices:
            self.add_vertex(f)
        if t not in self.vertices:
            self.add_vertex(t)
        self.vertices[f].add_neighbour(t)
        self.vertices[t].add_neighbour(f)
    
    def remove_edge(self, f, t):
        if f in self.vertices and t in self.vertices:
          self.vertices[f].remove_neighbour(t)
    
    def connection_existance(self, f, t):
        if f in self.vertices:
            return self.vertices[f].connection_existance(t)
        else:
          print("NIE")

    def number_of_connections(self, f):
        if f in self.vertices:
          return self.vertices[f].number_of_connections()
        else:
          print(0)

if __name__ == '__main__':
    G = Graph()
    n, m =  map(int, input().split())

    for x in range(m):
        stdin = input().split()
        c  = int(stdin[0])
        v1 = int(stdin[1])
        if len(stdin) == 3:
          v2 = int(stdin[2])

        if c == 1:
            G.add_edge(v1, v2)
        elif c == 2:
            G.remove_edge(v1, v2)
        elif c == 3:
            G.connection_existance(v1, v2)
        elif c == 4:
            G.number_of_connections(v1)


