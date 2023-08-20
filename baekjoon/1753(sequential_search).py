# 1753

# <by 순차탐색>

import sys

INF = int(1e9)

V , E = map(int, sys.stdin.readline().split()) # 정점 / 간선 

start = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)]

distance = [INF for _ in range(V+1)]

visited = [False for _ in range(V+1)]

for _ in range(E) :
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))

# 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 번호 반환
def get_smaller_node() :
    min_value = INF
    index = 0
    for i in range(1,V+1) :
        if not visited[i] and min_value > distance[i] :
            min_value = distance[i]
            index = i
    return index

# 다익스트라
def dijkstra() :
    distance[start] = 0
    visited[start] = True

    # 일단 출발노드의 인접노드에 대해서 최단거리 테이블에 넣기
    for a,b in graph[start] : # (2,2) , (3,3)
        distance[a] = b

    for _ in range(V-1) : # 이때 (V-1) 인 이유? : start 제외하고 모든 노드 검사하기 위해
        now = get_smaller_node()
        visited[now] = True
        for a,b in graph[now] : # (3,4),(4,5)
            cost = distance[now] + b
            if cost < distance[a] :
                distance[a] = cost

dijkstra()


for i in range(1,V+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])










    
