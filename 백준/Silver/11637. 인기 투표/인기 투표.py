t = int(input())
for i in range(t):
    arr = []
    n = int(input())
    for j in range(n):
        m = int(input())
        arr.append(m)
    a = sum(arr)
    b = max(arr)
    if arr.count(b) > 1:
        print('no winner')
    elif a/b < 2:
        print('majority winner', end=' ')
        print(arr.index(b)+1)
    elif a/b >= 2:
        print('minority winner', end=' ')
        print(arr.index(b)+1)