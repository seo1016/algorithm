n = int(input())
cnt = 0

if n<=5:
    print(0)
    exit()

for i in range(2, n+1, 2):
    nCopy = n
    nCopy -= i

    for j in range(1, nCopy+1):
        for k in range(nCopy-1, 0, -1):
            if k-j>=2 and j+k==nCopy and j!=0 and k!=0:
                cnt += 1

print(cnt)