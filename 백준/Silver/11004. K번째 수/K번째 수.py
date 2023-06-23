n, m = map(int, input().split())
a = list(map(int, input().split()))
arr = []
for i in a:
    arr.append(i)
arr.sort()
print(arr[m-1])