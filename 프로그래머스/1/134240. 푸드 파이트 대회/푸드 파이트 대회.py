def solution(food):
    answer = ''
    cnt = 0
    for i in food[1:]:
        if i==1:
            cnt += 1
            continue
        else:
            cnt += 1
            for i in range(i//2):
                answer += str(cnt)
    answer_reverse = answer[::-1]
    answer += '0'
    answer += answer_reverse
    return answer