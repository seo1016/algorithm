def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    first_cnt = 0
    second_cnt = 0
    third_cnt = 0
    for i in range(len(answers)):
        if answers[i] == first[i%len(first)]:
            first_cnt += 1
        if answers[i] == second[i%len(second)]:
            second_cnt += 1
        if answers[i] == third[i%len(third)]:
            third_cnt += 1
    maxx = max(first_cnt, second_cnt, third_cnt)
    if first_cnt == maxx:
        answer.append(1)
    if second_cnt == maxx:
        answer.append(2)
    if third_cnt == maxx:
        answer.append(3)
    return answer