t = int(input())
for i in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    print(min(m), end=' ')
    print(max(m))