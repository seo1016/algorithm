import sys
t = int(sys.stdin.readline())
arr = []
for i in range(t):
    n = int(sys.stdin.readline())
    arr.append(n)
arr.sort(reverse=True)
for i in arr:
    print(i)