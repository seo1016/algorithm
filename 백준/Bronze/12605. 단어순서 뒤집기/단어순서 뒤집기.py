t = int(input())
arr = []
n = 1
for i in range(1, t+1):
    a = input().split()
    for j in a:
        arr.append(j)
    arr.reverse()
    print("Case #%d: " %i, end='')
    for k in arr:
        print(k, end=' ')
    print()
    arr.clear()