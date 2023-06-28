a, b, c = map(int, input().split())
arr = []

arr.append(a)
arr.append(b)
arr.append(c)
arr.sort()
n = input()
for i in n:
    if i == 'A':
        print(arr[0], end=' ')
    elif i == 'B':
        print(arr[1], end=' ')
    else:
        print(arr[2], end=' ')