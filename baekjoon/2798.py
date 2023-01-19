# 2798 번 (블랙잭)
import itertools 

m, n = map(int,input().split())

arr = list(map(int,input().split()))

per_arr = (itertools.permutations(arr, 3))

max_num = 0

for i in per_arr :
    if sum(i)<=n :
        max_num = max(sum(i),max_num)

print(max_num)
