def solution(d, budget):
    answer = 0
    cnt = 0
    d.sort()
    for i in d:
        if answer + i <= budget:
            answer += i
            cnt += 1
        else:
            break
    return cnt