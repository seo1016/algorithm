arr = list(map(int, input().split()))

maxx = max(arr)
arr.remove(maxx)

while sum(arr) <= maxx:
    maxx -= 1

print(sum(arr)+maxx)