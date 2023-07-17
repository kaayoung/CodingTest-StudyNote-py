# 9663

import sys

N = int(sys.stdin.readline())

arr = [0]*N

answer = 0
visited = [False]*N

def is_possible(x) :
    for i in range(x) :
        if arr[x] == arr[i] or abs(x-i)== abs(arr[x]-arr[i]) :
            return False        
    return True

def dfs(x) :
    global answer

    if x==N :
        answer += 1
        return
    else : 
        for i in range(N) :
            if visited[i] :
                continue
            arr[x] = i
            if is_possible(x) :
                visited[i] = True
                dfs(x+1)
                visited[i] = False

dfs(0)
print(answer)
