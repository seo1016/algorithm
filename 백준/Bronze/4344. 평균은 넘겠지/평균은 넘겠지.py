t = int(input())
for i in range(t):
    aver = 0
    cnt = 0
    n = list(map(int, input().split()))
    n.pop(0)
    for j in n:
        aver += j
    for k in range(len(n)):
        if aver/len(n) < n[k]:
            cnt += 1
    cnt = cnt / len(n) * 100
    print("%.3f" %cnt, end='')
    print("%")