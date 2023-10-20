# 숫자의 표현

def solution(n):
    cnt = 0
    for i in range(1,n+1)  :
        if check(i,n) :
            cnt+=1
            
    return cnt

def check(start, result) :
    sum = 0
    while True :
        sum += start
        if sum == result :
            return True
        elif sum < result :
            start += 1 
        else :
            return False 
