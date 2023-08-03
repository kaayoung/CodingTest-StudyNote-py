# 5214

import sys
from collections import deque

N,K,M = map(int, sys.stdin.readline().split())

stations = [[] for _ in range(N+1)] # 해당 역의 하이퍼튜브 담음
hypers = [[] for _ in range(M+1)] # 해당 하이퍼 의 역들을 담음

for m in range(1,M+1) : # 하이퍼 번호
    station_list = list(map(int, sys.stdin.readline().split()))
    for s in station_list : # 해당 하이퍼의 역 번호
        stations[s].append(m)
        hypers[m].append(s)


stations_visited = [False for _ in range(N+1)]
hypers_visited = [False for _ in range(M+1)]

def bfs(start) :
    q = deque()
    q.append((start,1)) # 이동한 역 변호 / 방문 횟수
    stations_visited[start] = True

    while q :
        arr = [] # 바로 갈 수 있는 하이퍼 번호 리스트 / 초기화함 (ex: 1번역에서의 하이퍼는 1,2)
        q_station , q_visit = q.popleft()

        if q_station == N : # N번역 일 경우
            print(q_visit)
            return True
    
        for qh in stations[q_station] : # 해당 역의 하이퍼들
            if not hypers_visited[qh] : # 해당 하이퍼 방문 체 
                arr.append(qh) # 해당 역의 하이퍼 번호를 리스트에 추가 
                hypers_visited[qh] = True
        for hy in arr : 
            for s in hypers[hy] : # 갈수있는 역번호                 
                if not stations_visited[s] :
                    q.append((s,q_visit+1))
                    stations_visited[s] = True
    return False

if not bfs(1) :
    print(-1)
