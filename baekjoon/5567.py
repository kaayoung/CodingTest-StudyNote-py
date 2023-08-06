# 5567

import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

friends = [[] for _ in range(N+1)]

for _ in range(M) :
    a,b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

visited = [False for _ in range(N+1)]
visited[1] = True

def f() :
    q = deque()
    q.append((1,0)) # 친구 / 초대하는 동기의 수

    while q :
        qh_friend , qh_invited = q.popleft() 
        for friend in friends[qh_friend] :
            if qh_invited == 2 :
                print(visited.count(True)-1)
                return True
            if not visited[friend]:
                visited[friend]=True
                q.append((friend, qh_invited + 1))
    return False

if not f() :
    print(0)
