n = int(input())
b = 0
c = 0
for i in range(n):
    a = input()
    b = 0
    c = 0
    for i in range(len(a)):
        if a[i] == 'O':
            b += 1+c
            c += 1
        elif a[i] =='X':
            c = 0
    print(b)