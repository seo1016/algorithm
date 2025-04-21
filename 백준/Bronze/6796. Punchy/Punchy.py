A = 0
B = 0

while True:
    parts = input().split()
    op = int(parts[0])

    if op == 7:
        break

    if op == 1:
        var = parts[1]
        val = int(parts[2])
        if var == 'A':
            A = val
        else:
            B = val

    elif op == 2:
        var = parts[1]
        print(A if var == 'A' else B)

    elif op == 3:
        var1 = parts[1]
        var2 = parts[2]
        if var1 == 'A':
            A += A if var2 == 'A' else B
        else:
            B += A if var2 == 'A' else B

    elif op == 4:
        var1 = parts[1]
        var2 = parts[2]
        if var1 == 'A':
            A *= A if var2 == 'A' else B
        else:
            B *= A if var2 == 'A' else B

    elif op == 5:
        var1 = parts[1]
        var2 = parts[2]
        if var1 == 'A':
            A -= A if var2 == 'A' else B
        else:
            B -= A if var2 == 'A' else B

    elif op == 6:
        var1 = parts[1]
        var2 = parts[2]
        if var1 == 'A':
            A = int(A / A) if var2 == 'A' else int(A / B)
        else:
            B = int(B / A) if var2 == 'A' else int(B / B)