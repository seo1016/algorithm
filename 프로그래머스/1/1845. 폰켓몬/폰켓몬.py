def solution(nums):
    length = len(nums)
    nums = set(nums)
    set_length = len(nums)
    if length//2 < set_length:
        return length//2
    else:
        return set_length