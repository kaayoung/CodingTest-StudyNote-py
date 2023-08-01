# 1697

import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())

dist = [0] * (10**5 +1)

def bfs() :
    q = deque()
    q.append(n)

    while q :
        x = q.popleft()
        if x == k :
            print(dist[x])
            return
        for i in (x-1, x+1, 2*x) :
            if 0 <= i <= 10**5 and not dist[i] :
                dist[i] = dist[x] + 1
                q.append(i)



bfs()
    
