## 11047

import sys

n,k = map(int, sys.stdin.readline().split())
total = 0

arr = []

for i in range(n) :
    arr.append(int(sys.stdin.readline()))

for i in reversed(arr) :
    if k!=0 or i <= k :
        total = total + (k//i)
        k=k%i

print(total)
    
