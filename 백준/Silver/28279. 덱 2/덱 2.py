import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
deck = deque()
for i in range(N):
    command = input().split()
    if command[0] == '1':
        deck.appendleft(command[1])
    elif command[0] == '2':
        deck.append(command[1])
    elif command[0] == '3':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
            deck.popleft()
    elif command[0] == '4':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])
            deck.pop()
    elif command[0] == '5':
        print(len(deck))
    elif command[0] == '6':
        if len(deck) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == '7':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
    elif command[0] == '8':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])