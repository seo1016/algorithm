import sys
import math

input = sys.stdin.readline

n = int(input())
trees = [int(input()) for _ in range(n)]

diffs = []
for i in range(1, n):
    diffs.append(trees[i] - trees[i-1])

gcd = diffs[0]
for i in range(1, len(diffs)):
    gcd = math.gcd(gcd, diffs[i])

result = 0
for diff in diffs:
    result += (diff // gcd - 1)

print(result)