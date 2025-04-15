def draw_star(n):
    if n == 1:
        return ['*']
    
    prev = draw_star(n // 3)
    stars = []

    for i in range(n):
        if i // (n // 3) == 1:
            stars.append(prev[i % (n // 3)] + ' ' * (n // 3) + prev[i % (n // 3)])
        else:
            stars.append(prev[i % (n // 3)] * 3)

    return stars

n = int(input())
result = draw_star(n)
for line in result:
    print(line)