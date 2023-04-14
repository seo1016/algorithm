n = int(input())
fibo = [1, 1]
if n == 0:
     print("0")
     exit()
for i in range(2, n+1):
     fibo.append(fibo[i-1] + fibo[i-3])
print(fibo[n-2])