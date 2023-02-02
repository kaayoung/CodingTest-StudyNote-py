# 2609번

a,b = map(int, input().split())

def gcd(x,y) :
    while y > 0:
        x, y = y,x%y
    return x


print(gcd(a,b))

def lcd(x,y) :
    return x*y//gcd(x,y)

print(lcd(a,b))
