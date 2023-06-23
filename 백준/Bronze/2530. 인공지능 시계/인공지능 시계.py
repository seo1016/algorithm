h, m, s = map(int, input().split())
n = int(input())
s += n
while True:
    if h < 24 and m < 60 and s < 60:
        break
    elif s >= 60:
        m += s//60
        s = s%60
    elif m >= 60:
        h += m//60
        m = m%60
    elif h >= 24:
        h -= 24
print(h, m, s)
