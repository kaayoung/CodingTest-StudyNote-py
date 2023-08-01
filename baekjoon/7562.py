# 7562

import sys
from collections import deque

T = int(sys.stdin.readline())

results = []

def getCorList(x,y) :
    return [(x-1,y-2),(x+1,y-2),(x+2,y-1),(x+2,y+1),(x+1,y+2),(x-1,y+2),(x-2,y+1),(x-2,y-1)]

for _ in range(T) :
    I = int(sys.stdin.readline())
    graph = [[0 for _ in range(I)] for _ in range(I)]
    
    x,y = map(int , sys.stdin.readline().split())
    
    mx,my = map(int , sys.stdin.readline().split())

    q = deque()
    q.append((x,y))

    while q :
        qh = q.popleft()
        if qh == (mx,my) :
            results.append(graph[mx][my])
            break
        for c in getCorList(qh[0],qh[1]):
            if 0<= c[0] < I and 0<= c[1] < I and not graph[c[0]][c[1]]:
                q.append(c)
                graph[c[0]][c[1]] = graph[qh[0]][qh[1]] + 1

for r in results :
    print(r)
