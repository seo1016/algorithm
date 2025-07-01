def solution(x, n):
    answer = []
    x_copy = x
    cnt = 0
    while True:
        if cnt == n:
            break
        else:
            answer.append(x_copy)
            x_copy += x
            cnt += 1
    return answer