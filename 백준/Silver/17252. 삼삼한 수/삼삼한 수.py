n = int(input())

if n == 0:
    print("NO")
    exit()

is_samsam = True
while n > 0:
    if n % 3 > 1:
        is_samsam = False
        break
    n //= 3

print("YES" if is_samsam else "NO")