t = int(input())
arr = []
for i in range(t):
    a = input()
    arr.append(a)
if arr == sorted(arr, reverse=True):
    print('DECREASING')
elif arr == sorted(arr):
    print('INCREASING')
else:
    print('NEITHER')