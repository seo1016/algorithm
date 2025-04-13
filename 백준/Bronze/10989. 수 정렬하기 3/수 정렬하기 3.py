import sys

input = sys.stdin.readline
count = [0] * 10001

for _ in range(int(input())):
    count[int(input())] += 1

write = sys.stdout.write
for i in range(1, 10001):
    for _ in range(count[i]):
        write(f"{i}\n")