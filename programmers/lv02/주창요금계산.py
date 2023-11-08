# 주차 요금 계산


import math

def solution(fees, records):    
    d_time , d_fee , per_time, per_fee = fees
    answer_dic = {} # {"5961" : 100}
    result = []
    
    for record in records : 
        time, car_num , io = record.split()
        hour, minute = map(int, time.split(":"))
        time_to_minutes = (hour*60 + minute)
        if io == 'IN' : 
            time_to_minutes *= -1
        if car_num not in answer_dic.keys() :
            answer_dic[car_num] = 0
        answer_dic[car_num] += time_to_minutes
        
    answer_dic = sorted(answer_dic.items())
    for num,time in answer_dic :       
        if time <= 0 : 
            time += 23*60 + 59
        if time <= d_time : 
            result.append(d_fee)
        else : 
            result.append(d_fee+(math.ceil((time-d_time)/per_time))*per_fee)
    
    return result
