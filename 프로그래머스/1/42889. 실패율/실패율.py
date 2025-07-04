def solution(N, stages):
    answer = []
    fail = {}
    all_player = len(stages)
    for i in range(1, N+1):
        if all_player == 0:
            fail[i] = 0
        else:
            fail[i] = stages.count(i)/all_player
            all_player -= stages.count(i)
    answer = sorted(fail, key=lambda x:fail[x], reverse=True)
    return answer