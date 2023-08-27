# 이분탐색 - 반복문

import sys

def binary_search(arr, target, start, end) :
    while start <= end :
        mid = (start + end) // 2

        if arr[mid] == target :
            return mid

        if arr[mid] > target :
            end = mid - 1
        else :
            start = mid + 1
    return None

n,target = list(map(int, sys.stdin.readline().split()))

arr = list(map(int, sys.stdin.readline().split()))

result = binary_search(arr, target, 0 , n-1)

if result == None :
    print("원소 존재 X")
else :
    print(result + 1)
    
