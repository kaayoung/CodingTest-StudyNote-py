# 15686

import sys
import itertools

n,m = map(int, sys.stdin.readline().split())

graph = []

chicken = [] # 치킨집 좌표 리스트
chicken_comb = [] # 치킨집 M개의 조합 경우의 수의 리스트
house = [] # 집 좌표 리스트

dis = 0

for _ in range(n) :
    arr = list(map(int, sys.stdin.readline().split()))
    graph.append(arr)

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            house.append((i,j))
        if graph[i][j] == 2 :
            chicken.append((i,j))

arr = []

for combs in itertools.combinations(chicken,m) : # ((1,2),(2,2))
    dis_total = 0
    for i in house :
        dis = 10**4
        for comb in combs : # (1,2)
            dis = min(dis,abs(comb[0]-i[0]) + abs(comb[1] - i[1]))
        dis_total += dis
    arr.append(dis_total)

print(min(arr))
