N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]

ranks = []

for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    ranks.append(str(rank))

print(" ".join(ranks))