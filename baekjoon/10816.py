# 10816

import sys

N = int(sys.stdin.readline())
selected_cards = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
check_cards = list(map(int,sys.stdin.readline().split()))

selected_cards.sort()

def binary(start, end, num) :
    if start > end :
        return 0
    mid = (start + end) // 2
    
    if selected_cards[mid] == num :
        total = selected_cards[start:end+1].count(num)
        return total
    elif selected_cards[mid] < num :
       return binary(mid+1,end, num)
    else :
        return binary(start,mid-1 , num)



start_index , end_index = 0 , N-1

dic = {}

for i in check_cards :
    if i not in dic :
        dic[i] = binary(start_index,end_index,i)

print(" ".join(str(dic[i]) for i in check_cards))
