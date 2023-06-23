t = int(input())
for i in range(t):
    a = 0
    arr = []
    n = list(map(int, input().split()))
    for j in range(len(n)):
        if n[j] % 2 == 0:
            a += n[j]
            arr.append(n[j])
        else:
            continue
    print(a, end=' ')
    print(min(arr))