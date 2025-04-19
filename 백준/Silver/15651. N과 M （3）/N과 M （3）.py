def backtrack(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return

    for i in range(1, N + 1):
        result.append(i)
        backtrack(depth + 1)
        result.pop()

N, M = map(int, input().split())
result = []

backtrack(0)