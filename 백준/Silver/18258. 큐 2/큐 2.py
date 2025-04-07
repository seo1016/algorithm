import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
que = deque()

for _ in range(t):
    a = input().rstrip().split()

    if a[0] == 'push':
        que.append(a[1])

    elif a[0] == 'pop':
        if not que:
            print(-1)
        else:
            print(que.popleft())

    elif a[0] == 'size':
        print(len(que))
    
    elif a[0] == 'empty':
        print(0 if que else 1)

    elif a[0] == 'front':
        print(que[0] if que else -1)

    elif a[0] == 'back':
        print(que[-1] if que else -1)