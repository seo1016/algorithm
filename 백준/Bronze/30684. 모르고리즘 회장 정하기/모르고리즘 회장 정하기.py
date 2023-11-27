t = int(input())
arr = []
for i in range(t):
    a = input()
    if len(a) == 3:
        arr.append(a)
arr.sort()
print(arr[0])