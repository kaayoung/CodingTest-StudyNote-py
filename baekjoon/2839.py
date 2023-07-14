# 2839

import sys

n = int(sys.stdin.readline())
count = 0

while n>0 :
    if n%5 == 0 :
        count += n//5
        break
    else :
        if n < 3 :
            count = -1
            break
        else : 
            n -= 3
            count += 1 
print(count)
