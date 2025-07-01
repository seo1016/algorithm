def solution(n):
    answer = ''
    arr = []
    for i in str(n):
        arr.append(i)
    arr.sort(reverse=True)
    for i in arr:
        answer += str(i)
    return int(answer)