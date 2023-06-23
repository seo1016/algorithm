S = list(input())
T = list(input())
for i in range(len(T)-len(S)):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()
if S == T:
    print(1)
else:
    print(0)