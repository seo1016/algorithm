n = int(input())

low = 1
high = n
ans = []

for i in range(n):
    if i % 2 == 0:
        ans.append(high)
        high -= 1
    else:
        ans.append(low)
        low += 1

print(*ans)