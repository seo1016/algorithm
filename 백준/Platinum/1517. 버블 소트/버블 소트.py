import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def merge_sort(arr):
    def merge_sort_inner(start, end):
        nonlocal swap_count
        if end - start <= 1:
            return arr[start:end]

        mid = (start + end) // 2
        left = merge_sort_inner(start, mid)
        right = merge_sort_inner(mid, end)

        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                swap_count += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        arr[start:end] = merged
        return arr[start:end]

    swap_count = 0
    merge_sort_inner(0, len(arr))
    return swap_count

n = int(input())
a = list(map(int, input().split()))
print(merge_sort(a))