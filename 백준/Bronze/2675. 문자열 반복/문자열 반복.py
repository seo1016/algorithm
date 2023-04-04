T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    string = S
    repeat_count = R
    for char in string:
        for _ in range(repeat_count):
            print(char, end='')
    print()