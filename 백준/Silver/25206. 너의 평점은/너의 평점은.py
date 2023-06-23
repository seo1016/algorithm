arr = []
n = 0
m = 0
for i in range(20):
    a, b, c = input().split()
    b = float(b)
    if c == 'A+':
        n += b*4.5
        m += b
    elif c == 'A0':
        n += b*4.0
        m += b
    elif c == 'B+':
        n += b*3.5
        m += b
    elif c == 'B0':
        n += b*3.0
        m += b
    elif c == 'C+':
        n += b*2.5
        m += b
    elif c == 'C0':
        n += b*2.0
        m += b
    elif c == 'D+':
        n += b*1.5
        m += b
    elif c == 'D0':
        n += b*1.0
        m += b
    elif c == 'F':
        n += b*0.0
        m += b
    elif c == 'P':
        continue
if m == 0:
    print("%.6f" %m)
else:
    print("%.6f" %(n/m))