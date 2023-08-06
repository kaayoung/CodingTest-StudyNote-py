# 9461

import sys

T = int(sys.stdin.readline())

ans = []

dp = [0 for _ in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1

for _ in range(T) :
    N = int(sys.stdin.readline())
    for n in range(4,N+1) :
        if dp[n]==0 :
            dp[n] = dp[n-3] + dp[n-2]
    ans.append(dp[N])

for a in ans :
    print(a)
