import math

def solution(number, limit, power):
    arr = []
    for i in range(1, number+1):
        cnt = 0
        if i == 1:
            arr.append(1)
        else:
            for j in range(1, int(math.sqrt(i))+1):
                if i%j == 0:
                    if j == i // j:
                        cnt += 1
                    else:
                        cnt += 2
        arr.append(cnt)
    for i in range(len(arr)):
        if arr[i] > limit:
            arr[i] = power
    return sum(arr)