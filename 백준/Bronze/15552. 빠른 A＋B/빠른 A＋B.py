import sys
t = int(sys.stdin.readline())
for _ in range(t):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    print(sum(a))