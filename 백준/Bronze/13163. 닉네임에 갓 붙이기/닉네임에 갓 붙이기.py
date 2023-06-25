t = int(input())
for i in range(t):
    arr = []
    a = input().split()
    a.pop(0)
    for j in a:
        arr.append(j)
    print("god", end='')
    for k in arr:
        print(k, end='')
    print()