import sys
t = int(sys.stdin.readline())
for i in range(t):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    print("Case #", end='')
    print(i+1, end='')
    print(':', end=' ')
    print(sum(a))