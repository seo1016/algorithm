t = int(input())
n = list(map(int, input().split()))
if t == 1:
    print('koosaga')
    exit()
else:
    ans = n[0]
    for i in range(1,len(n)):
        ans = ans ^ n[i]
    if ans == 0:
        print('cubelover')
    else:
        print('koosaga')