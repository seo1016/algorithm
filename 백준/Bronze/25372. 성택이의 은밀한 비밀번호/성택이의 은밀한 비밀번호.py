t = int(input())
for i in range(t):
    n = 0
    a = input()
    for i in a:
        n += 1
    if 6 <= n <= 9:
        print('yes')
    else:
        print('no')