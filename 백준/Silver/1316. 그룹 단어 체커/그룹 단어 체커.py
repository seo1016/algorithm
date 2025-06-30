N = int(input())

cnt = 0
for _ in range(N):
    word = input()
    before = word[0]
    arr = [before]
    for i in word:
        if before == i:
            continue
        elif before != i and i not in arr:
            arr.append(i)
            before = i
        else:
            cnt += 1
            break

print(N-cnt)