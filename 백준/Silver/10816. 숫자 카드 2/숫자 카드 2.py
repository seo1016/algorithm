from collections import Counter

N = int(input())
cards = list(map(int, input().split()))
card_count = Counter(cards)

M = int(input())
targets = list(map(int, input().split()))

result = [card_count[t] for t in targets]

print(' '.join(map(str, result)))