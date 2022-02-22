first_chair_weight = int(input())
second_chair_weight = int(input())
third_chair_weight = int(input())
fourth_chair_weight = int(input())

maximum = max(first_chair_weight, second_chair_weight, third_chair_weight, fourth_chair_weight)

if maximum == first_chair_weight:
    print('1')
elif maximum == second_chair_weight:
    print('2')
elif maximum == third_chair_weight:
    print('3')
elif maximum == fourth_chair_weight:
    print('4')
