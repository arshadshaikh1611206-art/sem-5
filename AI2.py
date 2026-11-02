import heapq

edges = {
    ('A','C',2),
    ('D','B',1),
    ('A','D',3),
    ('B','C',4)
}

graph = {}
for a,b,c in edges:
    graph.setdefault(a, []).append((b,c))
    graph.setdefault(b, []).append((a,c))
    
h = {
    'A': 3,
    'B': 1,
    'C': 2,
    'D': 0
}

def best_first_search(start,goal):
    pq = [(h[start], start, [start])]
    visited = set()

    while pq:
        _,n,path = heapq.heappop(pq)
        if n == goal: return path
        if n in visited: continue
        visited.add(n)

        for v,_ in graph[n]:
            if v not in visited:
                heapq.heappush(pq, (h[v], v, path+[v]))
    return visited

print(best_first_search('A','D'))

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    visited = set()
    
    while pq:
        f,g,n,path = heapq.heappop(pq)
        if n == goal: return path,g
        if n in visited: continue
        visited.add(n)
        
        for v,cost in graph[n]:
            if v not in visited:
                ng = g + cost
                heapq.heappush(pq, (ng + h[v], ng, v, path+[v]))
    return visited
print(astar('A','D'))
