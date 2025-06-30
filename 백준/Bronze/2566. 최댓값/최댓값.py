arr = []
for i in range(9):
    n = list(map(int, input().split()))
    arr.append(n)

maxx = arr[0][0]
column = 1
row = 1
for j in range(9):
    for k in range(9):
        if arr[j][k] > maxx:
            maxx = arr[j][k]
            column = j+1
            row = k+1

print(maxx)
print(column, row)