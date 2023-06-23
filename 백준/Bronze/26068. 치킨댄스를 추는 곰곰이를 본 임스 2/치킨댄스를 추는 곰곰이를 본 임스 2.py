u = 0
n = int(input())
for i in range(n):
    a, b = input().split('-')
    b = int(b)
    if b<=90:
        u += 1
print(u)