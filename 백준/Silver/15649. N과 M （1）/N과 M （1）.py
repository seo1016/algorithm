def backtrack(N, M, sequence):
    if len(sequence) == M:
        print(*sequence)
        return
    
    for i in range(1, N+1):
        if i not in sequence:
            sequence.append(i)
            backtrack(N, M, sequence)
            sequence.pop()

N, M = map(int, input().split())

backtrack(N, M, [])