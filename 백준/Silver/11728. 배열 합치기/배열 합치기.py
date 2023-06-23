n, m = map(int, input().split())
arr = []
if n == 1:
    a = int(input())
    arr.append(a)
else:
    a = list(map(int, input().split()))
    for i in a:
        arr.append(i)
if m == 1:
    b = int(input())
    arr.append(b)
else:
    b = list(map(int, input().split()))
    for i in b:
        arr.append(i)
arr.sort()
for i in arr:
    print(i, end=' ')