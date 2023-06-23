t = int(input())
arr = []
for i in range(t):
    a, b = input().split()
    arr.append([int(a), b])
arr.sort(key= lambda y:y[0])
for i in arr:
    print(*i)