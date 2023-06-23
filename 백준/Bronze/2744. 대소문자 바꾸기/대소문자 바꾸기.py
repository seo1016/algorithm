a = input()
arr = []
for i in a:
    if chr(65) <= i <= chr(90):
        i = i.lower()
    else:
        i = i.upper()
    arr.append(i)
for j in arr:
    print(j, end='')