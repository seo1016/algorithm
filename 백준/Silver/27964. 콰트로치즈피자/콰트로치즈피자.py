n = int(input())
t = set(input().split())

cheese_count = 0
for topping in t:
    if topping.endswith("Cheese"):
        cheese_count += 1

if cheese_count >= 4:
    print("yummy")
else:
    print("sad")