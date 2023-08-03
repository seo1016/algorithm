a = input()
arr = []
for i in a:
    arr.append(i)
if arr[2] == '+':
    if int(arr[0]) + int(arr[4]) == int(arr[-1]):
        print("YES")
    else:
        print("NO")
elif arr[2] == '-':
    if int(arr[0]) - int(arr[4]) == int(arr[-1]):
        print("YES")
    else:
        print("NO")
elif arr[2] == '*':
    if int(arr[0]) * int(arr[4]) == int(arr[-1]):
        print("YES")
    else:
        print("NO")
elif arr[2] == '/':
    if int(arr[0]) / int(arr[4]) == int(arr[-1]):
        print("YES")
    else:
        print("NO")