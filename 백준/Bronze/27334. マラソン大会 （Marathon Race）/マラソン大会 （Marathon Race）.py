t = int(input())
n = list(map(int, input().split()))
arr = []
for i in n:
    arr.append(i)
arr.sort()
for i in n:
    print(arr.index(i)+1)