# Bartosz Bronikowski
# REPORTAZ - Reportaż dookoła świata 15.01.2022

from queue import Queue


def main():
    n, m =  map(int, input().split())
    keys = [i for i in range(n)]
    adj_list = {key: [] for key in keys}

    for i in range(m):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)       
      
    visited = {}
    level = {}
    queue = Queue()

    for node in adj_list.keys():
        visited[node] = False
        level[node] = -1
    
    s = 0
    visited[s] = True
    level[s] = 0
    queue.put(s)

    while not queue.empty():
        u = queue.get()
        
        for vertex in adj_list[u]:
            if not visited[vertex]:
                visited[vertex] = True
                level[vertex] = level[u] + 1
                queue.put(vertex)
    
    out = {k: v for k, v in sorted(level.items(), key= lambda item: (item[1], item[0]), reverse = True) if v > -1}

    for v in out.keys():
      print(v, end = ' ')


if __name__ == '__main__':
    main()
