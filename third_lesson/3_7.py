first_tourist_role = str(input())
second_tourist_role = str(input())
third_tourist_role = str(input())

member_price = 10
children_price = 5
not_member_price = 30
militia_price = 5

member = 'Член профсоюза'
children = 'Ребенок'
not_member = 'Не член профсоюза'
militia = 'Милиционер'

if first_tourist_role == member:
    first_price = member_price
elif first_tourist_role == children:
    first_price = children_price
elif first_tourist_role == not_member:
    first_price = not_member_price
else:
    first_price = militia_price

if second_tourist_role == member:
    second_price = member_price
elif second_tourist_role == children:
    second_price = children_price
elif second_tourist_role == not_member:
    second_price = not_member_price
else:
    second_price = militia_price

if third_tourist_role == member:
    third_price = member_price
elif third_tourist_role == children:
    third_price = children_price
elif third_tourist_role == not_member:
    third_price = not_member_price
else:
    third_price = militia_price

print(first_price + second_price + third_price)