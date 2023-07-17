# 10974

import sys

n = int(sys.stdin.readline())

arr = []

def d() :
    if len(arr) == n :
        print(" ".join(map(str, arr)))
        return
    for i in range(1,n+1) :
        if i in arr : continue
        arr.append(i)
        d()
        arr.pop()

d()
