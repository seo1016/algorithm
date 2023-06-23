import sys
N = int(input())
list = []
for i in range(N):
    a = sys.stdin.readline().rstrip().split()
    if a[0] == 'push':
        list.append(a[1])
    elif a[0] == 'pop':
        if len(list) == 0:
            print('-1')
        elif len(list) != 0: 
            print(list[0])
            list.pop(0)
    elif a[0] == 'size':
        print(len(list))
    elif a[0] == 'empty':
        if len(list) == 0:
            print("1")
        else:
            print("0")
    elif a[0] == 'front':
        if len(list) == 0:
            print(-1)
        else:
            print(list[0])
    elif a[0] == 'back':
        if len(list) == 0:
            print(-1)
        else:
            print(list[-1])