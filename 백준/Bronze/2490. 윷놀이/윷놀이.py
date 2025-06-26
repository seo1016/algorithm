for i in range(3):
    cnt = 0
    arr = list(map(int, input().split()))
    for j in arr:
        if j == 0:
            cnt += 1
    if cnt == 0:
        print("E")
    elif cnt == 1:
        print("A")
    elif cnt == 2:
        print("B")
    elif cnt == 3:
        print("C")
    elif cnt == 4:
        print("D")