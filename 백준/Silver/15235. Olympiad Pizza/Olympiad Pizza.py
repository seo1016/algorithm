from collections import deque

n = int(input())
slices = list(map(int, input().split()))

remaining = slices[:]
result = [0] * n

queue = deque((i, remaining[i]) for i in range(n))

time = 0

while queue:
    i, need = queue.popleft()
    time += 1
    need -= 1

    if need == 0:
        result[i] = time
    else:
        queue.append((i, need))

print(' '.join(map(str, result)))