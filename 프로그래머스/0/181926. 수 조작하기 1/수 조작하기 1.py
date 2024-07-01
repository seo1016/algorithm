def solution(n, control):
    answer = n
    arr = list(control)
    for i in arr:
        if i == 'w':
            answer += 1
        elif i == 's':
            answer -= 1
        elif i == 'd':
            answer += 10
        elif i == 'a':
            answer -= 10
    return answer