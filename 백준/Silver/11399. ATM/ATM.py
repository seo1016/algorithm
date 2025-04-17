n = int(input())
times = list(map(int, input().split()))

times.sort()

total_time = 0
accumulated = 0
for t in times:
    accumulated += t
    total_time += accumulated

print(total_time)