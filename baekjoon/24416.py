# 24416번

n = int(input())

d = [0] * 100
def f(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = f(x-1) + f(x-2)
    cnt[0] += 1  
    return d[x]

cnt = [0]

print(f(n), cnt[0])
print(cnt)
