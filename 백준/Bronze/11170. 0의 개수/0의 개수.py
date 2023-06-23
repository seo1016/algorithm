t = int(input())
for i in range(t):
    a = 0
    n, m = map(int, input().split())
    for j in range(n, m+1):
        for k in str(j):
            if k == '0':
                a += 1
            else:
                continue
    print(a)