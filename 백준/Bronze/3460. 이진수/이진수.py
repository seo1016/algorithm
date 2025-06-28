T = int(input())
for _ in range(T):
    n = int(input())
    b = bin(n)
    trim = b[2:]
    reverse = trim[::-1]
    for i in range(len(reverse)):
        if reverse[i] == '1':
            print(i, end=" ")
    print()