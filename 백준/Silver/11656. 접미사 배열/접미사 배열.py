a = input()
arr = []
for i in range(len(a)):
    if i == 0:
        arr.append(a)
    else:
        a = a[1:]
        arr.append(a)
arr.sort()
for i in arr:
    print(i)