n = int(input())

for _ in range(n):
    s = int(input())
    cnt = True

    for i in range(2, 1000000):
        if s%i==0:
            print("NO")
            cnt = False
            break

    if cnt == True:
        print("YES")