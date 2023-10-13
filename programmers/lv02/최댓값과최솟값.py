# 최댓값과 최솟값

def solution(s):
    arr = list(map(int, s.split()))
    return str(min(arr)) + ' ' +  str(max(arr))
