from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
tech = list(map(int, input().split()))

deck = deque()

for i in range(N-1, -1, -1):
    card = N - i
    if tech[i] == 1:
        deck.appendleft(card)
    elif tech[i] == 2:
        if len(deck) >= 1:
            first = deck.popleft()
            deck.appendleft(card)
            deck.appendleft(first)
        else:
            deck.appendleft(card)
    else:
        deck.append(card)

print(*deck)