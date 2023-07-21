# 2961

import sys
import itertools

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 1e9

for i in range(1,N+1) :
    combinations = itertools.combinations(arr,i) # [([1,7],[2,6]),([3,8],[4,9])]
    for com in combinations : # ([1,7],[2,6])
        s , m = 0 , 1
        for j in com : # [1,7]
            m *= j[0]
            s += j[1]
        
        ans = min(ans,abs(s-m))

print(ans)
