A = int(input())
B = int(input())
C = int(input())
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

num = str(A*B*C)
for i in num:
    arr[int(i)] += 1

for i in arr:
    print(i)