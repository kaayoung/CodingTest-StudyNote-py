# 약수의 합

def solution(n):
    sum = 0
    for i in range(1,n+1) : # 주의 : 0은 나누면 안됨 !!
        if n%i == 0 :
            sum += i
    return sum

def solution2(n):
    return n + sum([i for i in range(1,n//2+1) if n%i==0])
