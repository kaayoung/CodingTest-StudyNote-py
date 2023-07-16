# 2805

import sys

N , M = map(int, sys.stdin.readline().split())

tree_list = list(map(int, sys.stdin.readline().split()))

start , end = 0 , max(tree_list)

while start <= end :
    mid = (start + end) // 2
    total = 0

    for i in tree_list :
        if i <= mid :
            continue
        else :
            total += (i - mid)
            
    if total >= M :
        start = mid + 1
    else :
        end = mid - 1

print(end)
