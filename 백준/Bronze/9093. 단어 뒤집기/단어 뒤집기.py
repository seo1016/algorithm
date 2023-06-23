t = int(input())
for i in range(t):
    arr = []
    a = input().split()
    for i in a:
        i = i[::-1]
        arr.append(i)
    print(*arr)
