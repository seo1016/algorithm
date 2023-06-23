from sys import stdin
t = int(stdin.readline().rstrip())
arr = []
for i in range(t):
    a, b = stdin.readline().rstrip().split()
    if b == "enter":
        arr.append(a)
    elif b == "leave":
        arr.remove(a)
arr.sort(reverse=True)
for j in arr:
    print(j)