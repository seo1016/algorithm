arr = []
a = input()
for i in a:
    arr.append(i)

arr_1 = []
for j in a:
    arr_1.append(j)
arr_1.reverse()
if arr == arr_1:
    print(1)
else:
    print(0)