n, m = input().split()
arr = [n.replace('6', '5'), m.replace('6','5')]
arr_2 = [n.replace('5','6'), m.replace('5', '6')]
arr = map(int, arr)
arr_2 = map(int, arr_2)
print(sum(arr), sum(arr_2))