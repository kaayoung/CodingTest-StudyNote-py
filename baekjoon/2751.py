## 2751
import sys

num = int(sys.stdin.readline())
arr = []

for i in range(num) :
    n = int(sys.stdin.readline())
    arr.append(n)

arr.sort()

for i in arr :
    print(i)
