
import sys

t = int(input())
arr = []
for i in range(t):
    n = sys.stdin.readline().rstrip().split()
    if n[0] == '1':
        arr.append(n[-1])

    elif n[0] == '2':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
            arr.pop(-1)

    elif n[0] == '3':
        print(len(arr))

    elif n[0] == '4':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    
    elif n[0] == '5':
        if len(arr) >= 1:
            print(arr[-1])
        else:
            print(-1)