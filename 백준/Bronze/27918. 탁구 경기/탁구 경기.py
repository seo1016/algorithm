n = int(input())
D = 0
P = 0
for i in range(n):
    a = input()
    if D+2 == P or P+2 == D:
        D+=0
    elif a == 'D':
        D+=1
    elif a == 'P':
        P+=1
print(D, end='')
print(":", end='')
print(P)