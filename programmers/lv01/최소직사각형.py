# 최소직사각형

def solution(sizes):
    max_arr = []
    min_arr = []
    for size in sizes :
        a,b = min(size) , max(size)
        min_arr.append(a)
        max_arr.append(b)
    
    return max(min_arr)*max(max_arr)
