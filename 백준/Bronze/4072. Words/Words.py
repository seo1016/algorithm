while True:
    arr = []
    a = input().split()
    if a[0] == '#':
        break
    else:
        for i in a:
            i = i[::-1]
            arr.append(i)
        print(*arr)