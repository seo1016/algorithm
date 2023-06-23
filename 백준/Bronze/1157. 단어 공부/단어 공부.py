a = input().upper()
arr = []
for i in range(65, 91):
    arr.append(a.count(chr(i)))
if (arr.count(max(arr)) > 1):
    print("?")
else:
    n = int(arr.index(max(arr)))
    print(chr(65+n))