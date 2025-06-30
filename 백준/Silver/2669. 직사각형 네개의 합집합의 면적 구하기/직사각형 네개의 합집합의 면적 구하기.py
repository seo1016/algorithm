arr = [[0]*100 for _ in range(100)]

for _ in range(4):
    x, y, n, m = map(int, input().split())
    for i in range(x, n):
        for j in range(y, m):
            arr[i][j] = 1

cnt = 0
for k in range(100):
    cnt += arr[k].count(1)

print(cnt)