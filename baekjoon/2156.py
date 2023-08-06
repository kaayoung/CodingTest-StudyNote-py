# 2156

import sys

N = int(sys.stdin.readline())

wine = [0 for _ in range(10001)]

arr = [0 for _ in range(10001)]

for n in range(1,N+1) :
    wine[n]= int(sys.stdin.readline())


arr[1] = wine[1]
arr[2] = wine[1] + wine[2]
arr[3] = max(arr[2] , wine[2]+wine[3] , wine[1]+wine[3])

for i in range(3, N+1) :
    arr[i] = max(arr[i-2] + wine[i],arr[i-3] + wine[i] + wine[i-1],arr[i-1])

print(arr[N])

