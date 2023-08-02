# 14395

import sys
from collections import deque

s,t = map(int, sys.stdin.readline().split())

def cal(s, num) :
    if s == '*' :
        return num*num
    elif s == '+' :
        return num+num
    elif s == '/' :
        return 1
    else :
        return


if s==t :
    print(0)
elif t == 1 :
    print('/')
else :
    visited = set()
    ans = -1
    q = deque()
    q.append((s,''))
    while q :
        qh_num , qh_method = q.popleft()
        if qh_num == t :
            ans = qh_method
            break
        for i in ['*' , '+' , '/'] :
            nxt = cal(i,qh_num)
            if nxt <= 10**9 and nxt not in visited :
                q.append((nxt, qh_method+i))
                visited.add(nxt)

    print(ans)
