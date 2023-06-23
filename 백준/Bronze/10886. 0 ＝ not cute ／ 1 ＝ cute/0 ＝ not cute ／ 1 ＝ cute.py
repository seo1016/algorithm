t = int(input())
a = 0
b = 0
for i in range(t):
    n = int(input())
    if n == 1:
        a += 1
    elif n == 0:
        b += 1
if a > b:
    print('Junhee is cute!')
elif a < b:
    print('Junhee is not cute!')