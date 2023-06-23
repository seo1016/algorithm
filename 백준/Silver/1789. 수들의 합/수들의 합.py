a = 0
b = 1
n = int(input())
while True:
    a += b
    b += 1
    if n == a:
        b += 1
        break
    elif a > n:
        break
print(b-2)