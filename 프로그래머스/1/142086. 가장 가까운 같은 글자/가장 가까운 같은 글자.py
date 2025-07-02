def solution(s):
    answer = []
    arr = []
    for i in s:
        if i not in arr:
            answer.append(-1)
            arr.append(i)
        else:
            arr.reverse()
            answer.append(arr.index(i)+1)
            arr.reverse()
            arr.append(i)
    return answer