import sys

input = sys.stdin.readline

N = int(input())
yes_dance = set()
yes_dance.add("ChongChong")
for i in range(N):
    person1, person2 = input().split()

    if person1 in yes_dance:
        yes_dance.add(person2)
    elif person2 in yes_dance:
        yes_dance.add(person1)

print(len(yes_dance))