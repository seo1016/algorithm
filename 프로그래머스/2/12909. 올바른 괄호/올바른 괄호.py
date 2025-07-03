from collections import deque

def solution(s):
    arr = deque()
    for i in s:
        if i==')' and len(arr)==0:
            return False
        elif i==')' and len(arr)!=0:
            arr.popleft()
        elif i=='(':
            arr.append(i)
    if len(arr)==0:
        return True
    else:
        return False