# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
num = input('Введите число = ')
my_list = num.split('.')
a = abs(int(my_list[0]))
sum_a = 0
sum_b = 0
while a > 0:
    sum_a = sum_a + a % 10
    a = a // 10
if len(my_list) > 1:
    b = int(my_list[1])
    while b > 0:
        sum_b = sum_b + b % 10
        b = b //10       
sum = sum_a + sum_b
print(f'Сумма цифр числа {num} = {sum}')
    