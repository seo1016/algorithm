import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int,input().split()))
arr = []
for i in m:
    s = str(i)
    leng = len(s)
    while len(s) < 10:
        s += s[len(s)-leng]
    arr.append(([*list(s)],str(i)))
arr.sort(key = lambda x : x[0], reverse = True)
ans = ''
for i in arr:
    ans += i[-1]
print(ans if int(ans) != 0 else 0)