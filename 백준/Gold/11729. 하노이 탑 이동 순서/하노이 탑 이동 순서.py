def hanoi(n, start, end, temp, result):
    if n == 1:
        result.append((start, end))
        return
    hanoi(n - 1, start, temp, end, result)
    result.append((start, end))
    hanoi(n - 1, temp, end, start, result)

n = int(input())
result = []

hanoi(n, 1, 3, 2, result)

print(len(result))
for move in result:
    print(*move)