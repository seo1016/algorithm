s1, s2 = map(int, input().split())

if s1 == 0:
    print("H")

elif s2/s1 <= 2:
    print("E")

else:
    print("H")