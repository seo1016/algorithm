def solution(num_list):
    answer = 0
    multi = 1
    plus = 0
    for i in num_list:
        multi *= i
        plus += i
    if multi < plus**2:
        answer = 1
    else:
        answer = 0
    return answer