a, b, c = map(int, input().split())
arr = []
arr.append(a)
arr.append(b)
arr.append(c)
arr.sort(reverse=True)
print(arr[0]+arr[1])