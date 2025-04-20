n = int(input())
for _ in range(n):
    numbers = list(map(int, input().split()))
    print(' '.join(map(str, numbers)))
    
    has_17 = 17 in numbers
    has_18 = 18 in numbers

    if has_17 and has_18:
        print("both")
    elif has_17:
        print("zack")
    elif has_18:
        print("mack")
    else:
        print("none")
    print()