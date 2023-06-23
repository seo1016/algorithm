t = int(input())
for i in range(t):
    a = 0
    n = list(map(int, input().split()))
    for j in n:
        a += j
    print(a)