# 16953

import sys

a,b = map(int,sys.stdin.readline().split())

answer = 1

while b>a :
    
    if (b%10)!=1 and (b%10)%2==1 :
        answer = -1
        break ;
    elif b%10 == 1 : # 끝에 1일때
         b = b//10
         answer += 1
    else : # 끝에 짝수일 때
        b = b//2
        answer += 1
if a!=b : print(-1)
else : print(answer)
