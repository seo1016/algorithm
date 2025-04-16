import sys
input = sys.stdin.readline

t1 = int(input())
a = set(map(int, input().split()))
t2 = int(input())
b = list(map(int, input().split()))

for num in b:
    print(1 if num in a else 0, end=' ')