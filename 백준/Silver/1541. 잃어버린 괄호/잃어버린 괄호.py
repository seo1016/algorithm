arr = []
sentence = input().split('-')
for i in sentence:
    arr.append(sum(map(int, i.split('+'))))

result = arr[0]
for i in arr[1:]:
    result -= i

print(result)