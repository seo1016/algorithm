def solution(participant, completion):
    from collections import defaultdict
    
    counter = defaultdict(int)
    
    for p in participant:
        counter[p] += 1
    for c in completion:
        counter[c] -= 1
        
    for name in counter:
        if counter[name] > 0:
            return name