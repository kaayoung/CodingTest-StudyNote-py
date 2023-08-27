# 이진 탐색 - 재귀적 구현

import sys

def binary_search(arr, target, start, end) : # target 은 index 아니고 값 !!!
    if start > end :
        return None
    mid = (start + end) // 2

    if arr[mid]==target :
        return mid 

    if arr[mid] > target :
        return binary_search(arr,target,start,mid-1)
    else :
        return binary_search(arr,target,mid+1,end)

# n : 원소의 개수  /  target : 찾고자하는 값 
n, target = list(map(int , sys.stdin.readline().split()))

arr = list(map(int, sys.stdin.readline().split()))

result = binary_search(arr, target, 0 , n-1)

if result == None :
    print("없음")
else :
    print(result + 1)
