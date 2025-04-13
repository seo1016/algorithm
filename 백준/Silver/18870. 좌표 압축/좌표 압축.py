import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

sorted_unique = sorted(set(nums))

coordinate = {value: idx for idx, value in enumerate(sorted_unique)}

print(' '.join(str(coordinate[x]) for x in nums))