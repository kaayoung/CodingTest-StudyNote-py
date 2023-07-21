# 2606

import sys

count = int(sys.stdin.readline())

n = int(sys.stdin.readline())

graph = [[] for _ in range(count+1)]

ans = 0

for _ in range(n) : 
    a,b = map(int, sys.stdin.readline().split()) # 1, 2
    graph[a].append(b)
    graph[b].append(a)
    
# graph : [ [] , [2,5] , [1,3] , [2], [7], [1,2,6], [5] , [4] ]

visited = [False] * (count+1)

def dfs(i, visited) :
    visited[i] = True
    global ans
    ans += 1
    for k in graph[i] :
        if not visited[k] :
            dfs(k,visited)

dfs(1,visited)
print(ans-1)
