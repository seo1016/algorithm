t = int(input())
arr = []
for i in range(t):
    n, m = map(int, input().split())
    arr.append([n, m])
arr.sort(key=lambda x:(x[1],x[0]))
for i in arr:
    print(*i)