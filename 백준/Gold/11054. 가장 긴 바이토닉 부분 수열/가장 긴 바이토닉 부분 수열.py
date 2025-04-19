n = int(input())
A = list(map(int, input().split()))

inc = [1] * n
for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            inc[i] = max(inc[i], inc[j] + 1)

dec = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if A[j] < A[i]:
            dec[i] = max(dec[i], dec[j] + 1)

result = 0
for i in range(n):
    result = max(result, inc[i] + dec[i] - 1)

print(result)