n = int(input())
m = list(map(int, input().split()))
b = 0
for i in m:
    a = 0
    for j in range(1, i+1):
        if i%j == 0:
            a += 1
        else:
            continue
    if a == 2:
        b += 1
print(b)