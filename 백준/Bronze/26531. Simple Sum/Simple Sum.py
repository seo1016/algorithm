a = input()
if a[2] == '+':
    if int(a[0])+int(a[4]) == int(a[-1]):
        print("YES")
    else:
        print("NO")
elif a[2] == '-':
    if int(a[0])-int(a[4]) == int(a[-1]):
        print("YES")
    else:
        print("NO")
elif a[2] == '*':
    if int(a[0])*int(a[4]) == int(a[-1]):
        print("YES")
    else:
        print("NO")
elif a[2] == '/':
    if int(a[0])/int(a[4]) == int(a[-1]):
        print("YES")
    else:
        print("NO")