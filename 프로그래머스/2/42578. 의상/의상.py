def solution(clothes):
    answer = 1
    dic = {}
    for name, kind in clothes:
        if kind in dic:
            dic[kind].append(name)
        else:
            dic[kind] = [name]
    for kind in dic:
        answer *= (len(dic[kind])+1)
    return answer-1