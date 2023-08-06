# 1904

import sys

N = int(sys.stdin.readline())

arr = [0,1,2]


if N > 2 :
    for i in range(3,N+1) :
        arr.append((arr[i-2] + arr[i-1]) % 15746)
        
print(arr[N])
