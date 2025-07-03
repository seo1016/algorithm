def solution(n, m, section):
    answer = 0
    paint_end = 0
    for i in section:
        if i > paint_end:
            paint_end = i+m-1
            answer += 1
    return answer