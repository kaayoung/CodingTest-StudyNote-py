# 1753

# <by 힙>

import heapq
import sys

INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)]
distance = [INF for _ in range(V+1)]

for _ in range(E) :
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))

def dijkstra() :
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)
        
        # 순차탐색과 다르게 visited 테이블 대신 조건문으로 방문 여부 처리 !
        if distance[now] < dist :
            continue

        for a,b in graph[now] : # (2,2) (3,3)
            cost = distance[now] + b
            if cost < distance[a] :
                distance[a] = cost
                heapq.heappush(q,(cost, a))

dijkstra()

for i in range(1, V+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])
