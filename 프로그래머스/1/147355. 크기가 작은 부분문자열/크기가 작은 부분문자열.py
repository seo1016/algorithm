def solution(t, p):
    answer = 0
    if len(p) == 1:
        for i in t:
            if int(i) <= int(p):
                answer += 1
    else:
        for i in range(len(t)-len(p)+1):
            if int(t[i:i+len(p)]) <= int(p):
                answer += 1
    return answer