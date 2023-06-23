t = int(input())
arr = []
for i in range(t):
    arr.clear()
    n = list(map(int, input().split()))
    for i in n:
        arr.append(i)
    arr.sort(reverse=True)
    print(arr[2])
