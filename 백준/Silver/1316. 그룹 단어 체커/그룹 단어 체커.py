t = int(input())
b = 0
arr = []
for i in range(t):
    m = 0
    a = input()
    arr.clear()
    for i in range(len(a)):
        if i == 0:
            arr.append(a[i])
        elif a[i] in arr and a[i] != a[i-1]:
            m += 1
            break
        else:
            arr.append(a[i])
    if m == 0:
        b += 1
print(b)