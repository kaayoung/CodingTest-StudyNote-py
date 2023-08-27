# 이진탐색 - 라이브러리 이용

from bisect import bisect_left , bisect_right

def count_by_range(arr, left_value , right_value) :
    right_index = bisect_right(arr,right_value)
    left_index = bisect_left(arr,left_value)
    return right_index - left_index

arr = [1,2,3,3,3,3,4,4,8,9]


# 값이 4인 데이터 개수
print(count_by_range(arr,4,4))

# -1 ~ 3 범위에 있는 데이터 개수
print(count_by_range(arr,-1,3))
