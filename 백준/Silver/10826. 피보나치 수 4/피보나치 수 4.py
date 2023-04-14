n = int(input())
fibo = [1, 1]
if n == 0:
     print("0")
     exit()
for i in range(2, n):
     fibo.append(fibo[i-2] + fibo[i-1])
print(fibo[-1])