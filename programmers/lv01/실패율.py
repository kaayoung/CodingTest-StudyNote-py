# 실패율 

def solution(N, stages): 
    dic = {}
    players_cnt = len(stages) 
    
    for i in range(N) :
        if (players_cnt !=0) :
            dic[i+1] = stages.count(i+1) / players_cnt
            players_cnt -= stages.count(i+1)
        else :
            dic[i+1] = 0
    
    result = sorted(dic.keys(), key=lambda x : dic[x] , reverse=True)
    
    return result
