def solution(a, b, n):
    answer = 0
    remain = 0
    while True:
        if n >= a:
            remain += n%a
            exchanged = (n//a)*b
            answer += exchanged
            n = exchanged
        else:
            n += remain
            remain = 0
            if n < a:
                break
    return answer