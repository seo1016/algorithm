import math

def solution(n):
    answer = 0
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(math.sqrt(i)+1)):
            if i%j==0:
                is_prime = False
                break
        if is_prime:
            answer += 1
    return answer