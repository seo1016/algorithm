t = int(input())
n = list(map(int, input().split()))
n.sort()
for i in n:
    print(i, end=' ')