# 1789
import sys

s = int(sys.stdin.readline())

n = 0 

arr = [1]
i=1

while s>0 :
    if s-i == 0 or (s-i) <= i :
        n += 1
        break
    else :
        n += 1
        s = s-i
        i += 1
print(n)
