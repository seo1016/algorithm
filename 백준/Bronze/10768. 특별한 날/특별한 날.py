n = int(input())
m = int(input())
if n == 2 and m == 18:
    print("Special")
elif n < 2:
    print("Before")
elif n == 2 and m < 18:
    print("Before")
elif n > 2:
    print("After")
elif n == 2 and m > 18:
    print("After")