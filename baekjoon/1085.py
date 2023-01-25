# 1085번
import sys

x,y,w,h = map(int, sys.stdin.readline().split())

arr = []

arr.append(w-x)
arr.append(h-y)
arr.append(x)
arr.append(y)

print(min(w-x,h-y,x,y))
