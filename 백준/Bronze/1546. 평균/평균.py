N = int(input())
arr = list(map(int, input().split()))
answer = []
max_score = max(arr)
for i in range(N):
    answer.append(arr[i]/max_score*100)
print(sum(answer)/N)