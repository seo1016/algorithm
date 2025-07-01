def solution(n):
    arr = []
    for i in range(1, n+1):
        if n%i==0:
            arr.append(i)
            
    answer = sum(arr)
    return answer