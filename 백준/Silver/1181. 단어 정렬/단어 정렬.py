t = int(input())
arr = []
for i in range(t):
    a = input()
    if a in arr:
        continue
    else:
        arr.append(a)
arr.sort()
arr.sort(key=len)
for i in arr:
    print(i)