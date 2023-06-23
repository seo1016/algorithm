t = int(input())
arr = []
for i in range(t):
    n, m = map(int, input().split())
    arr.append([n, m])
arr.sort()
for i in arr:
    print(*i)