def solution(price, money, count):
    first_price = price
    arr = []
    for i in range(count):
        arr.append(price)
        price += first_price
    if sum(arr)-money > 0:
        return sum(arr)-money
    else:
        return 0