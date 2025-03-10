def solution(nums):
    answer = 0
    head_list = len(nums)
    head_set = len(set(nums))
    
    if head_list // 2 < head_set:
        answer = head_list // 2
    else:
        answer = head_set
        
    return answer