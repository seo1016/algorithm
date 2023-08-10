arr = []
for i in range(5):
    n = int(input())
    if n in arr:
        arr.remove(n)
    else:
        arr.append(n)
print(*arr)