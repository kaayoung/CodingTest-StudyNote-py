# 1946

import sys

t = int(sys.stdin.readline())

for i in range(t) :
    n = int(sys.stdin.readline())
    arr = [0]*n
    
    for j in range(n) :
        scores = list(map(int, sys.stdin.readline().split()))
        arr[j] = scores
        
    arr.sort(key=lambda x : x[0])

    count = 1
    m = arr[0][1]

    for j in range(1,n) :
        if arr[j][1] < m :
            m = arr[j][1]
            count+= 1 
        
    print(count)
