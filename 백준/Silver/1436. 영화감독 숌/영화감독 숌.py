import sys

input = sys.stdin.readline

N = int(input())
string = '666'
cnt = 0

while True:
    if '666' in string:
        cnt += 1

    if cnt == N:
        print(string)
        break
    string_int = int(string)
    string_int += 1
    string = str(string_int)