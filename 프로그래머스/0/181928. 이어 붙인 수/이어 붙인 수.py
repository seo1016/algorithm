def solution(num_list):
    answer = 0
    odd = ''
    even = ''
    for i in num_list:
        if i%2==1:
            i = str(i)
            odd += i
        elif i%2==0:
            i = str(i)
            even += i
    odd = int(odd)
    even = int(even)
    answer = odd+even
    return answer