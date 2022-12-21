# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
import random
import math
my_list = []
size = int(input('Введите размер списка = '))
for i in range(size):
   my_list.append(random.randint(0,10))
# print(my_list)
my_multipl_list = []

for i in range(math.ceil(len(my_list)/2)):
    my_multipl_list.append(my_list[i] * my_list[len(my_list)-1-i])
print(f'{my_list} => {my_multipl_list}')