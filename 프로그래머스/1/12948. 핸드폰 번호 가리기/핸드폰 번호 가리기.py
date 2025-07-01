def solution(phone_number):
    answer = ''
    arr = []
    for i in phone_number:
        arr.append(i)
    for i in range(len(arr)-4):
        arr[i] = '*'
    for i in arr:
        answer += i
    return answer