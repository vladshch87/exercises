transfer_type = int(input())
rub_gold_rate = int(input())
usd_gold_rate = int(input())
currency_amount = int(input())

if transfer_type == 1:
    result = rub_gold_rate / usd_gold_rate * currency_amount
    print(str(currency_amount) + ' Руб это ' + str(result) + ' $')
elif transfer_type == 2:
    result = usd_gold_rate / rub_gold_rate * currency_amount
    print(str(currency_amount) + ' $ это ' + str(result) + ' Руб')