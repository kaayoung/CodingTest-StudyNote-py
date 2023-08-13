# 2670

import sys

N = int(sys.stdin.readline())

arr = [float(sys.stdin.readline()) for _ in range(N)]

for i in range(1,N) :
    arr[i] = max(arr[i] , arr[i-1]*arr[i])

print(f'%0.3f' % max(arr))
