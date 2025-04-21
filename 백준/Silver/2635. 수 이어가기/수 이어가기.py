n = int(input())
max_sequence = []

for i in range(1, n+1):
    seq = [n, i]
    while True:
        next_num = seq[-2] - seq[-1]
        if next_num < 0:
            break
        seq.append(next_num)
        
    if len(seq) > len(max_sequence):
        max_sequence = seq

print(len(max_sequence))
print(*max_sequence)