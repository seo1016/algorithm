def solution(k, score):
    answer = []
    arr = []
    for i in score:
        if len(arr) == k:
            if i > arr[0]:
                arr.pop(0)
                arr.append(i)
        else:
            arr.append(i)
        arr.sort()
        answer.append(arr[0])
    return answer