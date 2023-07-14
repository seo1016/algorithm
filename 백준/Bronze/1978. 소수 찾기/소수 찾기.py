t = int(input())
n = list(map(int, input().split()))
plus = 0
for i in n:
    cnt = 0
    for j in range(2, i):
        if i%j == 0:
            cnt += 1
    if cnt == 0 and i != 1:
        plus += 1
print(plus)