import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    _ = input()
    _ = input()
    print("Yes" if n <= m else "No")