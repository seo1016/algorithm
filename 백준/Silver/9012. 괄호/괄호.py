t = int(input())
for i in range(t):
    a = input()
    arr = []
    for j in range(len(a)):
        arr.append(a[j])
        if len(arr) >= 2:
            if arr[-2:] == ["(",")"]:
                arr.pop()
                arr.pop()
    if arr == []:
        print("YES")
    else:
        print("NO")