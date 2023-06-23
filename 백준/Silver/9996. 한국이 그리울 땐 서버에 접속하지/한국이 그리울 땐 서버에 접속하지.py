t = int(input())
n, m = input().split('*')
for i in range(t):
    a = input()
    if len(n)+len(m) > len(a):
        print("NE")
    elif a[:len(n)] == n and a[-len(m):] == m:
        print("DA")
    else:
        print("NE")