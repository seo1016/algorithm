arr = []
a = 0
b = 0
for _ in range(7):
    n = int(input())
    if n%2 == 1:
        arr.append(n)
        b += 1
    else:
        continue
if b == 0:
    print("-1")
else:
    for i in arr:
        a += i
    print(a)
    print(min(arr))
