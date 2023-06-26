t = int(input())
for i in range(t):
    a, b = input().split()
    if b in a:
        a = a.replace(b, '1')
    print(len(a))