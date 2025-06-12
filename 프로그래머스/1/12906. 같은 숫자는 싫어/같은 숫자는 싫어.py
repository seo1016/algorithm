def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
            save = arr[i]
        else:
            if save == arr[i]:
                continue
            else:
                answer.append(arr[i])
                save = arr[i]
    return answer