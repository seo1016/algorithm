import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

summ = 0
for i in range(N):
    summ += A[i]*B[i]

print(summ)