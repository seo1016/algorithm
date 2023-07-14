n = int(input())
m = int(input())
arr = []
for i in range(n, m+1):
    cnt = 0
    for j in range(2, i):
        if i%j == 0:
            cnt += 1
    if cnt == 0 and i != 1:
        arr.append(i)
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))