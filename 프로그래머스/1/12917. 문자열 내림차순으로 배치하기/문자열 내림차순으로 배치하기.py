def solution(s):
    answer = ''
    upper = []
    lower = []
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            upper.append(i)
        else:
            lower.append(i)
    lower.sort(reverse=True)
    upper.sort(reverse=True)
    for i in lower:
        answer += i
    for i in upper:
        answer += i
    return answer