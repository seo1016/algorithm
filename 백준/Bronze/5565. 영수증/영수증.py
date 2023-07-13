n = int(input())
arr = []
for _ in range(9):
    m = int(input())
    arr.append(m)
for i in arr:
    n -= i
print(n)