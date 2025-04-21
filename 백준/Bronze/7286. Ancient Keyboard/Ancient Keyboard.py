t = int(input())
for _ in range(t):
    n = int(input())
    intervals = []
    max_time = 0

    for _ in range(n):
        ch, a, b = input().split()
        a, b = int(a), int(b)
        intervals.append((ch, a, b))
        max_time = max(max_time, b)

    leds_on = [0] * 26
    output = []

    for time in range(max_time):
        count = 0
        for ch, a, b in intervals:
            if a <= time < b:
                count += 1
        if count == 0:
            continue
        output.append(chr(ord('A') + count - 1))
    
    print(''.join(output))