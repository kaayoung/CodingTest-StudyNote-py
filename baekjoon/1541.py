# 1541

import sys

arr = sys.stdin.readline().split('-')
add_arr = []
# ['22','44+11+1',...]

for i in arr :
    if '+' in i :
        num_arr = list(map(int,i.split('+')))
        add_arr.append(sum(num_arr))
    else :
        add_arr.append(int(i))

# [22,54,12]
total = add_arr[0]
for i in range(1,len(add_arr)) :
    total -= add_arr[i]

print(total)
