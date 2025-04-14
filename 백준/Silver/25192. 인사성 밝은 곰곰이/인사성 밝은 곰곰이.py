import sys

input = sys.stdin.readline

N = int(input())
cnt = 0
nickname_set = set()

for i in range(N):
    nickname = input().strip()
    if nickname == 'ENTER':
        cnt += len(nickname_set)
        nickname_set.clear()
    else:
        nickname_set.add(nickname)

cnt += len(nickname_set)
print(cnt)