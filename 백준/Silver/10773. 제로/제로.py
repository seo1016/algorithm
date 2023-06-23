t = int(input())
arr = []
a = 0
for i in range(t):
    n = int(input())
    if n == 0:
        arr.pop(-1)
    else:
        arr.append(n)
for j in arr:
    a += j
print(a)