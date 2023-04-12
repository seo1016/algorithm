while True:
    s = input()
    cnt = 0
    if s == "#":
        break
    for i in s:
        if i in "AEIOUaeiou":
            cnt += 1
    print(cnt)