t = int(input())
result = 0
remain = 0

for _ in range(t):
    c, v = map(int, input().split())

    result = c//v
    remain = c%v

    print(f"You get {result} piece(s) and your dad gets {remain} piece(s).")