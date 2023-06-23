while True:
    arr = []
    a = input()
    if a == "END":
        break
    else:
        for i in a:
            arr.append(i)
        arr.reverse()
        for j in arr:
            print(j, end='')
        print()