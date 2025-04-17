import sys

def cantor(s, start, length):
    if length == 1:
        return
    third = length // 3
    for i in range(start + third, start + 2 * third):
        s[i] = ' '
    cantor(s, start, third)
    cantor(s, start + 2 * third, third)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    size = 3 ** n
    s = ['-'] * size
    cantor(s, 0, size)
    print(''.join(s))