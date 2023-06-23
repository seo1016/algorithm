while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if a>=b>=c and a>=b+c:
            print("Invalid")
        elif a>=c>=b and a>=b+c:
            print("Invalid")
        elif b>=a>=c and b>=a+c:
            print("Invalid")
        elif b>=c>=a and b>=a+c:
            print("Invalid")
        elif c>=b>=a and c>=a+b:
            print("Invalid")
        elif c>=a>=b and c>=a+b:
            print("Invalid")
        elif a == b == c:
            print('Equilateral')
        elif a == b != c or a != b == c or a == c != b:
            print('Isosceles')
        elif a != b != c:
            print('Scalene')