arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = input()
for i in a:
	arr[ord(i) - 97] += 1
for k in arr:
	print(k, end=' ')