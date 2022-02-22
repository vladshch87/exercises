goose_price = int(input())
amount = int(input())

if goose_price < 0 or amount < 0:
    print('Число не может быть отрицательным')
elif 5 < amount < 10:
    discount = goose_price * amount * 25 / 100
    print(int(goose_price * amount - discount))
elif amount > 10:
    print(int(goose_price * amount / 2))
else:
    print(int(goose_price * amount))