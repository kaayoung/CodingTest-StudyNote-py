## 25305

total, num = map(int, input().split(' '))
arr = list(map(int,input().split(' ')))
arr.sort(reverse=True)
print(arr[num-1])
