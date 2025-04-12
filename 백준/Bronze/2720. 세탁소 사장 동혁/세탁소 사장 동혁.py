T = int(input())

Quarter = 25
Dime = 10
Nickel = 5
Penny = 1

for i in range(T):
    C = int(input())
    print(C//Quarter, end=" ")
    C %= Quarter
    print(C//Dime, end=" ")
    C %= Dime
    print(C//Nickel, end=" ")
    C %= Nickel
    print(C//Penny)