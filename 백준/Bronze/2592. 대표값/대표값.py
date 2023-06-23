n = 0
arr = []
for i in range(10):
    a = int(input())
    arr.append(a)
    n += a
print(n//10)
print(max(arr, key=arr.count))