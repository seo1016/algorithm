N, M = map(int,input().split())
arr = list(map(int,input().split()))

maxx = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            summ = arr[i]+arr[j]+arr[k]
            if summ <= M and summ > maxx:
                maxx = summ

print(maxx)