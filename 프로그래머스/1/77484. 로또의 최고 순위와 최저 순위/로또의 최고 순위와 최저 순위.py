def solution(lottos, win_nums):
    answer = []
    dic = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    win = 0
    lose = 0
    cnt = 0
    for i in lottos:
        if i == 0:
            cnt += 1
        if i in win_nums:
            win += 1
        else:
            lose += 1
    answer.append(dic[win+cnt])
    answer.append(dic[win])
    return answer