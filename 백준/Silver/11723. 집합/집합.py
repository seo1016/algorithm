#집합을 구현하는 문제(11723)

from sys import stdin
S = 0b0
n = int(input())

for _ in range(n):
    cmd = stdin.readline().split()
    if len(cmd) == 1:
        if cmd[0] == 'all':
            S = 0b111111111111111111110
        else:
            S = 0
    else:
        cmd, x = cmd
        x = int(x)
        if cmd == 'add':
            S |= (1 << x)
        if cmd == 'remove':
            S &= ~(1 << x)
        if cmd == 'check':
            print(1 if S & (1 << x) else 0)
        if cmd == 'toggle':
            S ^= (1 << x)