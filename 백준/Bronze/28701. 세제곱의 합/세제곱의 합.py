n = int(input())
first = 0
third = 0
for i in range(1, n+1):
    first += i
    third += i**3
second = first**2
print(first)
print(second)
print(third)