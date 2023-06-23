import math # sqrt

def sieve(n):
    arr = [True] * (n+1)
    arr[0] = False; arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i]:
            j = 2
            while i*j <= n: 
                arr[i*j] = False
                j += 1
    return arr
a,b = map(int,input().split())
ar = sieve(b)
for i in range(len(ar)):
    if ar[i] != False:
        if i >= a:
            print(i)