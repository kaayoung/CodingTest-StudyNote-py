# 11404

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

INF = int(1e9)

arr = [[INF for _ in range(N+1)] for _ in range(N+1)]

for n in range(N+1) :
    arr[n][n] = 0

for _ in range(M) :
    a,b,c = map(int, sys.stdin.readline().split())
    if c < arr[a][b] :
        arr[a][b] = c

for k in range(1,N+1) : # 거치는 점
    for i in range(1,N+1) : # 시작 점
        for j in range(1,N+1) : # 끝 점
            arr[i][j] = min(arr[i][j] , arr[i][k]+arr[k][j])

for i in range(1,N+1) :
    for j in range(1,N+1) :
        if arr[i][j] >= INF :
            print(0, end=' ')
        else : 
            print(arr[i][j] , end=' ')
    print()
