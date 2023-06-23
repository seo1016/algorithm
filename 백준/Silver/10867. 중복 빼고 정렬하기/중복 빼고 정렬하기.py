t = int(input())
arr = []
n = set(map(int, input().split()))
for i in n:
    arr.append(i)
arr.sort()
print(*arr)