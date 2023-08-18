while True:
    yak = []
    n = int(input())
    if n == -1:
        break
    for i in range(1, n):
        if n%i == 0:
            yak.append(i)
    if n == sum(yak):
        print(f"{n} = ", end='')
        for i in yak:
            if i != yak[-1]:
                print(f"{i} + ", end='')
            elif i == yak[-1]:
                print(i)
    else:
        print(f"{n} is NOT perfect.")