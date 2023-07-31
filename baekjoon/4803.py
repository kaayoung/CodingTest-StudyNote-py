# 4803

import sys

sys.setrecursionlimit(10**6)

c = 0

def f(node, prev) :
    if visited[node] : # cycle 안됨
        return False
    visited[node] = True
    for i in graph[node] :
        if i!=prev :
            if not f(i,node) :
                return False 
    return True
            

while True :
    c += 1
    tree = 0
    n,m = map(int, sys.stdin.readline().split())
    if n==0 and m==0 :
        break

    graph = [[] for _ in range(n+1)]
    
    for _ in range(m) :
        x,y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [False for _ in range(n+1)]
    
    for i in range(1,n+1) :
        if visited[i] :
            continue
        if f(i,0) :
            tree += 1
    if tree == 0 :
        print(f"Case {c}: No trees.")
    elif tree == 1 :
        print(f"Case {c}: There is one tree.")
    else :
        print(f"Case {c}: A forest of {tree} trees.")
    
        
        
