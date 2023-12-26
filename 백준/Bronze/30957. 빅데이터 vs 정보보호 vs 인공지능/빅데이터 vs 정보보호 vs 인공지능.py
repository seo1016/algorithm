t = int(input())
a = input()
B = 0
S = 0
A = 0
for i in a:
    if i == "B":
        B += 1
    elif i == "S":
        S += 1
    elif i == "A":
        A += 1
if B==S==A:
    print("SCU")
else:
    if B>=S and B>=A:
        print("B", end='')
    if S>=B and S>=A:
        print("S", end='')
    if A>=S and A>=B:
        print("A", end='')
