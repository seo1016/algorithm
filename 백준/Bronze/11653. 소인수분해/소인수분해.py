n = int(input())
arr = []
while n != 0:
    a = 0
    for i in range(2, n+1):
        if n%i == 0:
            n = n//i
            a += 1
            arr.append(i)
            break
        else:
            continue
    if a == 0:
        for j in arr:
            print(j)
        exit()
    else:
        continue