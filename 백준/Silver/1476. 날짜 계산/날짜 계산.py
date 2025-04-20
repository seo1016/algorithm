E, S, M = map(int, input().split())

year = 1
while True:
    e = year % 15 if year % 15 != 0 else 15
    s = year % 28 if year % 28 != 0 else 28
    m = year % 19 if year % 19 != 0 else 19

    if e == E and s == S and m == M:
        print(year)
        break
    year += 1