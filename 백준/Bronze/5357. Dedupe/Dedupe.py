t = int(input())
for i in range(t):
    arr = []
    n = input()
    for i in n:
        if len(arr) == 0:
            arr.append(i)
        if i != arr[-1]:
            arr.append(i)
    for i in arr:
        print(i, end='')
    print()