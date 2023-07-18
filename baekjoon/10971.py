# 10971

import sys

n = int(sys.stdin.readline())

graph = [0]*n # 행렬
ans = sys.maxsize

for i in range(n) :
    graph[i] = list(map(int, sys.stdin.readline().split()))


def f(start, next, value,visited) :
    global ans
    if len(visited) == n :
        if graph[next][start] != 0 :
            ans = min(ans, value+graph[next][start])
        return
    for i in range(n) :
        if graph[next][i] != 0 and i not in visited and value < ans :
            visited.append(i)
            f(start, i , value + graph[next][i],visited)
            visited.pop()

for i in range(n) :
    f(i,i,0,[i])
print(ans)
