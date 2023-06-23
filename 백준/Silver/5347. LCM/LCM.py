import math
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    a = math.lcm(n, m)
    print(a)