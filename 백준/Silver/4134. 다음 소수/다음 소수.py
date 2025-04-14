import sys
import math

input = sys.stdin.readline

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    while True:
        if is_prime(n):
            print(n)
            break
        n += 1