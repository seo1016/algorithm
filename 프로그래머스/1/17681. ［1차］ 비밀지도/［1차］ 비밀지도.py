def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        merged = arr1[i] | arr2[i]
        str_bin = bin(merged)[2:].zfill(n)
        
        line = ''
        for j in str_bin:
            if j == '1':
                line += '#'
            else:
                line += ' '
        answer.append(line)
    return answer