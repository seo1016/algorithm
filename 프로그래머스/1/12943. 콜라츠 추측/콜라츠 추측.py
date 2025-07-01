def solution(num):
    cnt = 0
    if num == 1:
        return cnt
    while cnt != 500:
        cnt += 1
        if num%2 == 0:
            num //= 2
        else:
            num = num*3+1
        if num == 1:
            return cnt
    return -1