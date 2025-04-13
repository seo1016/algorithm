import sys

input = sys.stdin.readline

n = int(input())
x_list = []
y_list = []

for _ in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

min_x = min(x_list)
max_x = max(x_list)
min_y = min(y_list)
max_y = max(y_list)

area = (max_x - min_x) * (max_y - min_y)
print(area)