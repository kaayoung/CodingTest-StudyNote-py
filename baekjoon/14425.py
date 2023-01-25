# 14425번

import sys

n,m = map(int, sys.stdin.readline().split())
cnt = 0

s = set()

for _ in range(n) :
    s.add(sys.stdin.readline())

for _ in range(m) :
    mm = sys.stdin.readline()
    if mm in s : cnt += 1

print(cnt)
