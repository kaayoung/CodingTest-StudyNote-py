# 올바른 괄호 

def solution(s):
    arr = []
        
    for i in s :
        if i == '(' :
            arr.append(i)
        else :
            if arr == [] :
                return False
            else : 
                arr.pop()
    
    if len(arr)== 0 :
        return True 
    else :
        return False
