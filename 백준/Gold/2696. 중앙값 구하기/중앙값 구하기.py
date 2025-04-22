import heapq
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M = int(input())
    numbers = []
    while len(numbers) < M:
        numbers += list(map(int, input().split()))

    result = []
    max_heap = []
    min_heap = []

    for i in range(M):
        num = numbers[i]

        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        if i % 2 == 0:
            result.append(-max_heap[0])

    print(len(result))
    for i in range(0, len(result), 10):
        print(" ".join(map(str, result[i:i+10])))