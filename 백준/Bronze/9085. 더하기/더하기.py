t = int(input())
for i in range(t):
    a = 0
    n = int(input())
    m = list(map(int, input().split()))
    for j in range(len(m)):
        a += m[j]
    print(a)