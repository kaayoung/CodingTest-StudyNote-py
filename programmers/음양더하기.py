# 음양 더하기

def solution(absolutes, signs):
    # 첫 풀이 : 음수이면 하나하나 -1 곱한후 absolutes 의 sum을 구함
    answer = 0
    for i in range(len(signs)) :
        if not signs[i] :
            answer -= absolutes[i]
        else :
            answer += absolutes[i]
    
    return answer
