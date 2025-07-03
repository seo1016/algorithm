def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for i in photo:
        result = 0
        for j in i:
            result += dic.get(j, 0)
        answer.append(result)
    return answer