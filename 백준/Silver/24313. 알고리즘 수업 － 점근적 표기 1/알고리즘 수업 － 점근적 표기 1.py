n, m = map(int, input().split())
a = int(input())
b = int(input())
if n*b+m <= a*b and n<=a:
    print(1)
else:
    print(0)