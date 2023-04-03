N, M = map(int, input().split())
box = [0]*(N+1)
for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        box[n] = k
for i in range(1, N+1):
    print(box[i], end=' ')