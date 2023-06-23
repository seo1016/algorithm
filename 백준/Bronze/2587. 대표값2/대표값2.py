n = 0
arr = []
for i in range(5):
    a = int(input())
    arr.append(a)
    n += a
print(n//5)
arr.sort()
print(arr[2])