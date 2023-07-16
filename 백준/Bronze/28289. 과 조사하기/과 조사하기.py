t = int(input())
sw = 0
im = 0
ai = 0
first = 0
for i in range(t):
    a, b, c = map(int, input().split())
    if a == 1:
        first += 1
    elif b == 1 or b == 2:
        sw += 1
    elif b == 3:
        im += 1
    elif b == 4:
        ai += 1
print(sw)
print(im)
print(ai)
print(first)