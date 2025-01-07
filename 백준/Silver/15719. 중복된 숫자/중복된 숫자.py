import sys

n = int(input())
expected_total = sum(range(1, n))

sequence = sys.stdin.readline().strip()
current_sum = 0
partial_number = ""

for char in sequence:
    if char.isdigit():
        partial_number += char
    else:
        current_sum += int(partial_number)
        partial_number = ""

if partial_number:
    current_sum += int(partial_number)

print(current_sum - expected_total)