from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empty = []
virus = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

def spread_virus(temp):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))

def get_safe_area(temp):
    return sum(row.count(0) for row in temp)

max_safe = 0

for walls in combinations(empty, 3):
    temp = copy.deepcopy(lab)
    for wx, wy in walls:
        temp[wx][wy] = 1
    spread_virus(temp)
    max_safe = max(max_safe, get_safe_area(temp))

print(max_safe)