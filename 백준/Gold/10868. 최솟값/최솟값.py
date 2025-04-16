import sys
input = sys.stdin.readline

def build(node, start, end):
    if start == end:
        tree[node] = nums[start]
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def query(node, start, end, left, right):
    if right < start or end < left:
        return float('inf')
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    lmin = query(node * 2, start, mid, left, right)
    rmin = query(node * 2 + 1, mid + 1, end, left, right)
    return min(lmin, rmin)

N, M = map(int, input().split())
nums = [0] + [int(input()) for _ in range(N)]

tree = [0] * (4 * N)
build(1, 1, N)

for _ in range(M):
    a, b = map(int, input().split())
    print(query(1, 1, N, a, b))