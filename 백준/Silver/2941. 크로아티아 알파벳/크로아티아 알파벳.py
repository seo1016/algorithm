a = input()
b = 0
n = 0
arr = []
for i in a:
    arr.append(i)
while b < len(arr):
    if b+2 <= len(arr) and arr[b] == 'c' and arr[b+1] == '=':
        n += 1
        b += 2
    elif b+2 <= len(arr) and arr[b] == 'c' and arr[b+1] == '-':
        n += 1
        b += 2
    elif b+2 <= len(arr) and arr[b] == 'd' and arr[b+1] == '-':
        n += 1
        b += 2
    elif b+3 <= len(arr) and arr[b] == 'd' and arr[b+1] == 'z' and arr[b+2] == '=':
        n += 1
        b += 3
    elif b+2 <= len(arr) and arr[b] == 'l' and arr[b+1] == 'j':
        n += 1
        b += 2
    elif b+2 <= len(arr) and arr[b] == 'n' and arr[b+1] == 'j':
        n += 1
        b += 2
    elif b+2 <= len(arr) and arr[b] == 's' and arr[b+1] == '=':
        n += 1
        b += 2
    elif b+2 <= len(arr) and arr[b] == 'z' and arr[b+1] == '=':
        n += 1
        b += 2
    else:
        n += 1
        b += 1
print(n)