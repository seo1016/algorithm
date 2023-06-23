arr = []
arr_re = []
while True:
    arr.clear()
    arr_re.clear()
    a = input()
    if a == '0':
        break
    for i in a:
        arr.append(i)
    arr.reverse()
    for j in arr:
        arr_re.append(j)
    arr.reverse()
    if arr == arr_re:
        print("yes")
    else:
        print('no')