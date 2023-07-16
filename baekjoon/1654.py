# 1654

import sys

K , N = map(int, sys.stdin.readline().split())

arr = [0]*K

for i in range(K) :
    arr[i]= int(sys.stdin.readline())

start , end = 1 , max(arr)

while start <= end :
    mid = (start + end) // 2
    total = 0
    for i in arr :
        total += (i // mid)

    if total >= N :
        start = mid + 1
    else :
        end = mid - 1
print(end)
