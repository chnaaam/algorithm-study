menu = [int(input()) for _ in range(5)]
ham = menu[:3]
coke = menu[3:]

min_price = 10000
for h in ham:
    for c in coke:
        price = h + c - 50
        if price < min_price:
            min_price = price

print(min_price)
