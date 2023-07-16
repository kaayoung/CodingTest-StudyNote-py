# 2512

import sys

N = int(sys.stdin.readline())

req_list = list(map(int,sys.stdin.readline().split()))

req_list.sort()

M = int(sys.stdin.readline())

start , end = 0, req_list[N-1]

while start <= end :
    mid = (start + end) // 2

    sum_budget = 0
    for i in req_list :
        sum_budget += min(i,mid)
    if sum_budget > M :
        end = mid-1
    else :
        start = mid + 1
print(end)
