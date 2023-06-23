c, d, e, f, g, a, b, C = map(int, input().split())
if c == 1 and d == 2 and e == 3 and f == 4 and g ==5 and a == 6 and b == 7 and C == 8:
    print("ascending")
elif c == 8 and d == 7 and e == 6 and f == 5 and g == 4 and a == 3 and b == 2 and C == 1:
    print("descending")
else:
    print("mixed")