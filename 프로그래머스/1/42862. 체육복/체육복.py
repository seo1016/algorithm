def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    n -= len(lost_set)
    for i in lost_set:
        if i-1 in reserve_set:
            n += 1
            reserve_set.remove(i-1)
        elif i+1 in reserve_set:
            n += 1
            reserve_set.remove(i+1)
    return n