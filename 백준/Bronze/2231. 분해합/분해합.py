n = int(input())
for i in range(1, n+1):
    a = 0
    for j in str(i):
        a += int(j)
    if i+a == n:
        print(i)
        exit()
    else:
        continue
print(0)