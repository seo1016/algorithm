import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

lcm = math.lcm(b, d)

a *= lcm // b
c *= lcm // d

numerator = a + c
denominator = lcm

gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd

print(numerator, denominator)