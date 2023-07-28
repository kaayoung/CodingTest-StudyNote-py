# 1012

import sys

N = int(sys.stdin.readline())
sys.setrecursionlimit(10**6)

answers = []

def dfs(x,y) : # x : 가로  /  y : 세로 
    if x<0 or y<0 or x>=m or y>=n :
        return False
    if graph[y][x] == 1 :
        graph[y][x] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False 

for _ in range(N) :
    m,n,k = map(int, sys.stdin.readline().split())
    # m : 가로 (두번째)  /  n : 세로 (첫번째)
    graph = [[0] * m for _ in range(n)]
    for _ in range(k) :
        a,b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1
    cnt = 0
    
    for i in range(m) :
        for j in range(n) :
            if dfs(i,j) :
                cnt += 1
                
    answers.append(cnt)

for a in answers :
    print(a)
