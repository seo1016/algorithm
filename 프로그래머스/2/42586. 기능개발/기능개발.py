import math
from collections import Counter

def solution(progresses, speeds):
    arr = []
    for i in range(len(progresses)):
        arr.append(math.ceil((100-progresses[i])/speeds[i]))
    before = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < before:
            arr[i] = before
        else:
            before = arr[i]
    counter = Counter(arr)
    answer = list(counter.values())
    return answer