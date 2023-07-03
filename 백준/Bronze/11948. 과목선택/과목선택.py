arr = []
a = 0
for i in range(4):
    n = int(input())
    arr.append(n)
arr.sort(reverse=True)
arr.pop(-1)
for i in arr:
    a += i
arr.clear()
for i in range(2):
    n = int(input())
    arr.append(n)
arr.sort(reverse=True)
arr.pop(-1)
for i in arr:
    a += i
print(a)