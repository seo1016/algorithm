arr = list(map(int, input().split()))
while True:
    arr_sort = []
    for i in range(4):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            print(*arr)
    arr_sort = sorted(arr)
    if arr == arr_sort:
        break