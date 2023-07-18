# 7490

import sys

test_count = int(sys.stdin.readline())

arr = []

def f(n, num_arr) : # n : 부호 넣을 자리 수    
    if len(arr) == n :
        get_result(arr,num_arr)
        return
    for i in [' ', '+','-'] :
        arr.append(i)
        f(n,num_arr)
        arr.pop()

def get_result(arr , num_arr) :
    exp = ''
    for i in range(len(num_arr)) :
        if i==len(num_arr)-1 :
            exp += str(num_arr[len(num_arr)-1])
        else :
            exp += str(num_arr[i]) + arr[i]
    exp2 = exp.replace(' ','')
    if eval(exp2) == 0 :
        print(exp)


test_arr = [0]*test_count
for i in range(test_count) :
    test_arr[i] = int(sys.stdin.readline())
for i in range(len(test_arr)) :
    f(test_arr[i]-1 , [j for j in range(1,test_arr[i]+1)])
    if i != len(test_arr)-1 :
        print()
