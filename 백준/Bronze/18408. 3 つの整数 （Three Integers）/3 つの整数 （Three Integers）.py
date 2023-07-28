a, b, c = map(int, input().split())
n = 0
m = 0
if a == 1:
    n += 1
else:
    m += 1
if b == 1:
    n += 1
else:
    m += 1
if c == 1:
    n += 1
else:
    m += 1
if n>m:
    print(1)
else:
    print(2)