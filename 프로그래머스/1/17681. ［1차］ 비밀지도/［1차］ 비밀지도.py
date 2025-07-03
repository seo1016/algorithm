def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        merged = arr1[i] | arr2[i]
        bin_str = bin(merged)[2:].zfill(n)
        line = ''
        for i in bin_str:
            if i=='1':
                line+='#'
            else:
                line+=' '
        answer.append(line)
    return answer