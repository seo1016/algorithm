import sys
input = sys.stdin.readline

def build(start, end, node):
    if start == end:
        min_tree[node] = arr[start]
        max_tree[node] = arr[start]
        return
    mid = (start + end) // 2
    build(start, mid, node * 2)
    build(mid + 1, end, node * 2 + 1)
    min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1])
    max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1])

def query(start, end, node, left, right):
    if right < start or end < left:
        return (float('inf'), float('-inf'))
    if left <= start and end <= right:
        return (min_tree[node], max_tree[node])
    mid = (start + end) // 2
    lmin, lmax = query(start, mid, node * 2, left, right)
    rmin, rmax = query(mid + 1, end, node * 2 + 1, left, right)
    return (min(lmin, rmin), max(lmax, rmax))

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
min_tree = [0] * (4 * N)
max_tree = [0] * (4 * N)

build(0, N - 1, 1)

for _ in range(M):
    a, b = map(int, input().split())
    result = query(0, N - 1, 1, a - 1, b - 1)
    print(result[0], result[1])