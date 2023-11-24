# 땅따먹기

def solution(land):
    
    for l in range(1,len(land)) :
        for i in range(4) :
            land[l][i] += max(land[l-1][:i] + land[l-1][i+1:])
        
    return max(land[len(land)-1])
