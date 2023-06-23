arr = []
arr2 = []
arr3 = []
a = 0
for i in range(8):
    n = int(input())
    arr.append(n)
    arr2.append(n)
arr2.sort(reverse=True)
del arr2[5:]
for i in arr2:
    a += i
print(a)
for i in range(5):
    arr3.append(arr.index(arr2[i])+1)
arr3.sort()
print(*arr3)