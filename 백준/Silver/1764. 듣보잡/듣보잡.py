import sys

input = sys.stdin.readline

n, m = map(int, input().split())

listen_set = set()
for _ in range(n):
    listen_set.add(input().strip())

see_set = set()
for _ in range(m):
    see_set.add(input().strip())

result = sorted(listen_set & see_set)

print(len(result))
for name in result:
    print(name)