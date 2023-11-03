# 할인행사

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9) :
        temp_arr = discount[i:i+10]
        able = True
        for j in range(len(want)) :
            if number[j] > temp_arr.count(want[j]) : 
                able = False
                break
        if able :
            answer += 1
                
    return answer
