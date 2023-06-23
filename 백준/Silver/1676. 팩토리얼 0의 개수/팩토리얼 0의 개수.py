n = int(input())
a = 1
b = 0
for i in range(1, n+1):
    a *= i
arr = list(str(a))
arr.reverse()
for k in arr:
    if k == '0':
        b += 1
    else:
        break
print(b)