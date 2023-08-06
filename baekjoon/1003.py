# 1003

import sys

T = int(sys.stdin.readline())

answers = []

for _ in range(T) :
    z_cnt = [1,0]
    o_cnt = [0,1]

    N = int(sys.stdin.readline())

    if N > 1 :
        for i in range(2,N+1) :
            z_cnt.append(z_cnt[i-1] + z_cnt[i-2])
            o_cnt.append(o_cnt[i-1] + o_cnt[i-2])
    answers.append(f'{z_cnt[N]} {o_cnt[N]}')

for a in answers :
    print(a)
