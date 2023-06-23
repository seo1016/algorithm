a = int(input())
b = int(input())
c = int(input())

arr = [0 for i in range(10)]

d = 0
e = 0
f = 0
g = 0
h = 0
k = 0
l = 0
m = 0
n = 0
o = 0
z = a*b*c
z = str(z)

for j in z:
    if j == '0':
        d += 1
    elif j == '1':
        e += 1
    elif j == '2':
        f += 1
    elif j == '3':
        g += 1
    elif j == '4':
        h += 1
    elif j == '5':
        k += 1
    elif j == '6':
        l += 1
    elif j == '7':
        m += 1
    elif j == '8':
        n += 1
    elif j == '9':
        o += 1

print(d)
print(e)
print(f)
print(g)
print(h)
print(k)
print(l)
print(m)
print(n)
print(o)