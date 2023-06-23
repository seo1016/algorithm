n, m = map(int, input().split())
hei = 0
box = 0
if n == 0 or m == 0:
    print(0)
    exit()
else:
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if hei + a[i] > m:
            box += 1
            hei = a[i]
            continue
        hei += a[i]
        if hei == m:
            box += 1
            hei = 0
    if hei > 0:
        print(box+1)
    else:
        print(box)