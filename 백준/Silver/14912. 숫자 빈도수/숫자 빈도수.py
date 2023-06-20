n, m = map(int, input().split())
a = 0
for i in range(1, n+1):
    for j in str(i):
        if j == str(m):
            a += 1
        else:
            continue
print(a)