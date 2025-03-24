n = int(input())
for i in range(n):
    left = 0
    right = 0
    isTrue = True
    
    string = input()
    string = list(string)
    
    for j in string:
        if j == '(':
            left += 1
        else:
            if left != 0:
                left -= 1
            else:
                isTrue = False

    if isTrue and left == 0 and right == 0:
        print("YES")
    else:
        print("NO")