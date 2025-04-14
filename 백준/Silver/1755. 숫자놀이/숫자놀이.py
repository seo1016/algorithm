import sys

input = sys.stdin.readline

M, N = map(int, input().split())

dic = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

arr = list(range(M, N + 1))

arr.sort(key=lambda x: ' '.join(dic[d] for d in str(x)))

for i in range(len(arr)):
    print(arr[i], end=' ')
    if (i + 1) % 10 == 0:
        print()