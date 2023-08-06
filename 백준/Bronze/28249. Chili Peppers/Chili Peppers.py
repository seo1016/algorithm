t = int(input())
a = 0
for i in range(t):
    n = input()
    if n == 'Poblano':
        a += 1500
    elif n == 'Mirasol':
        a += 6000
    elif n == 'Serrano':
        a += 15500
    elif n == 'Cayenne':
        a += 40000
    elif n == 'Thai':
        a += 75000
    elif n == 'Habanero':
        a += 125000
print(a)