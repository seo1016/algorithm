n, m = map(int, input().split())
arr = []
z = 0
for i in range(n):
    a = input()
    arr.append(a)
for j in range(m):
    b = input()
    if b in arr:
        z += 1
    else:
        continue
print(z)