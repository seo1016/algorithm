N, M = map(int, input().split())
box = [i for i in range(1,N+1)]
for i in range(M):
    a, b = map(int, input().split())
    temp = box[a-1]
    box[a - 1] = box[b - 1]
    box[b - 1] = temp
for i in range(N):
    print(box[i], end = ' ')