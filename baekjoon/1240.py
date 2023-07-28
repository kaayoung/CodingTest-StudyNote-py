# 1240

import sys
sys.setrecursionlimit(10**6)

n,m = map(int, sys.stdin.readline().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(n-1) :
    x,y,d = map(int, sys.stdin.readline().split())
    graph[x][y] = d
    graph[y][x] = d

result = 0

def dfs(start , end , distance) : # start:시작하는 노드 / end:최종적으로 이동하려는 노드
    visited[start] = True
    global result 
    for i in range(1,n+1) :
        if graph[start][i] >0 and not visited[i] :
            if end == i :
                result = distance + graph[start][i]
                return
            else :
                dfs(i,end,distance+graph[start][i])


for _ in range(m) :
    x,y = map(int, sys.stdin.readline().split())
    visited = [False] * (n+1)
    dfs(x,y,0)
    print(result)

