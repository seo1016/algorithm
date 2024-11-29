t = int(input())
for _ in range(t):
    sentence = input()

    if sentence[-1] == '.':
        print(sentence)
    else:
        print(sentence, end='')
        print('.')