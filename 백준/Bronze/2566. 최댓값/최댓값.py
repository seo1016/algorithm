from collections import deque

dequee = deque()

for i in range(1, 10):
    arr = deque(map(int, input().split()))

    for j in arr:
        dequee.append(j)

maxx = max(dequee)
print(maxx)

indexx = dequee.index(maxx)+1
remain = indexx%9
if remain == 0:
    print(f"{indexx//9} 9")
else:
    print(f"{indexx//9+1} {remain}")