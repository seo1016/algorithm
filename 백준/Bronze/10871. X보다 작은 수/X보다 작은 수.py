N, X = map(int, input().split())
a = list(map(int, input().split()))
for i in range(N):
    if X>a[i]:
        print(a[i], end = ' ')
    else:
        continue