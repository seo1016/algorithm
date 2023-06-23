a = input()
n = 0
for i in a:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        n += 1
    else:
        continue
print(n)