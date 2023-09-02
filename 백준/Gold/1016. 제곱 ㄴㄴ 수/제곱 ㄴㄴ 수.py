minn, maxx = map(int,input().split())
arr = [i**2 for i in range(2, int(maxx**0.5)+1)]
num = [1] * (maxx-minn+1)
for i in arr:
    n = minn//i*i
    while(n < maxx+1):
        if n - minn >= 0:
            num[n-minn] = 0
        n += i
print(sum(num))