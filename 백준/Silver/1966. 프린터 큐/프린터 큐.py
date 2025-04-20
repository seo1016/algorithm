from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    count = 0

    while queue:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            count += 1
            if cur[0] == M:
                print(count)
                break