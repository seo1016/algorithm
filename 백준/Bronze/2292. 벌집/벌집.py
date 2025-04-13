n = int(input())
numbox = 1
cnt = 1

while n > numbox:
    numbox += 6 * cnt
    cnt += 1

print(cnt)