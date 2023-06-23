n = int(input())
a = 1
w = 0
if n == 1:
    print(1)
    exit()
while a**2 < n:
    if a**2 <= n:
        a += 1
        w += 1
print(w)