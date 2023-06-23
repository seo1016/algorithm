n = int(input())
arr = []
for i in str(n):
    arr.append(int(i))
arr.sort(reverse=True)
for j in arr:
    print(j, end='')
