a = input()
n = 0
for i in a:
    print(i, end='')
    n += 1
    if n == 10:
        print()
        n = 0