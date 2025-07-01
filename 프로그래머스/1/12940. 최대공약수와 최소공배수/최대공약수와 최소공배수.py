import math

def solution(n, m):
    answer = []
    answer.append(math.gcd(n, m))
    num = n
    while True:
        if num%n == 0 and num%m == 0:
            answer.append(num)
            break
        num+=n
    return answer