a = input()
arr = []
arr_2 = []
n = 0
for i in a:
    arr.append(i)
    arr_2.append(i)
arr_2.reverse()
if len(arr) == 1:
    print(-1)
elif arr.count(arr[0]) == len(arr):
    print(-1)
elif arr != arr_2:
    print(len(arr))
else:
    print(len(arr)-1)