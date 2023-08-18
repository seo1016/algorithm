f, s = [], []
n, m = map(int, input().split())
for i in range(n):
    a = list(map(int, input().split()))
    f.append(a)
for i in range(n):
    b = list(map(int, input().split()))
    s.append(b)
for i in range(n):
    for j in range(m):
        print(f[i][j]+s[i][j], end=" ")
    print()