#1934

import sys

n = int(sys.stdin.readline())
arr = []

def gcd(a,b):
    while b>0 :
        a , b = b, a%b
    return a

def lcd(a,b) :
    return a*b//gcd(a,b)

for _ in range(n) :
    a,b = map(int, sys.stdin.readline().split())
    arr.append(lcd(a,b))

for i in arr :
    print(i)
