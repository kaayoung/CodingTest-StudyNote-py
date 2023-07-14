# 11399

import sys

n = int(sys.stdin.readline())
total = 0

arr = list(map(int,sys.stdin.readline().split()))
l = len(arr)

arr.sort()

for i in arr :
    total += i*l
    l -= 1

print(total)
