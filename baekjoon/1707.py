# 1707

import sys
from collections import deque

K = int(sys.stdin.readline())

results = []

def bfs(start) :
    q = deque()
    q.append(start)
    colors[start] = 1
    while q :
        qh = q.popleft()
        for i in graph[qh] :
            if colors[i]==0 :
                q.append(i)
                colors[i] = -1 * colors[qh]
            elif colors[i]==colors[qh]:
                return False 
    return True
    

for _ in range(K) :
    V , E = map(int, sys.stdin.readline().split())
    bg = 'YES'
    graph = [[] for _ in range(V+1)]
    colors = [0 for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    for _ in range(E) :
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,V+1) :
        if colors[i] == 0 :
            if not bfs(i) :
                bg = 'NO'
                break
    results.append(bg)

for r in results  :
    print(r)
