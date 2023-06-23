t = int(input())
for i in range(1, t+1):
    arr = []
    n = list(map(int, input().split()))
    n.pop(0)
    n.sort()
    for j in range(len(n)):
            arr.append(n[j] - n[j-1])
    print("Class %d" %(i))
    print("Max %d, " %(max(n)), end='')
    print("Min %d, " %(min(n)), end='')
    print("Largest gap %d" %(max(arr)))