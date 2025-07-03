def solution(s):
    dic = {
        'zero':0, 
        'one':1, 
        'two':2, 
        'three':3, 
        'four':4, 
        'five':5, 
        'six':6, 
        'seven':7, 
        'eight':8, 
        'nine':9
    }
    save = ''
    answer = ''
    for i in s:
        if i.isdigit():
            answer += str(i)
        else:
            save += i
            if save in dic:
                answer += str(dic.get(save))
                save = ''
    return int(answer)