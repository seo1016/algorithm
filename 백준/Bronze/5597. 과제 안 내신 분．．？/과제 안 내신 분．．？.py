a = [i for i in range(1,31)]
arr = []
for i in range(28):
    n=int(input())
    arr.append(n)
for i in range(30):
    if a[i] not in arr:
        print(i + 1)