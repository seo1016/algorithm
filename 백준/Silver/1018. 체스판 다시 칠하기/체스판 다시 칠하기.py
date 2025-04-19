n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

def count_repaint(x, y, start_color):
    cnt = 0
    for i in range(8):
        for j in range(8):
            expected = start_color if (i + j) % 2 == 0 else ('B' if start_color == 'W' else 'W')
            if board[x + i][y + j] != expected:
                cnt += 1
    return cnt

min_repaint = 64
for i in range(n - 7):
    for j in range(m - 7):
        repaint_w = count_repaint(i, j, 'W')
        repaint_b = count_repaint(i, j, 'B')
        min_repaint = min(min_repaint, repaint_w, repaint_b)

print(min_repaint)