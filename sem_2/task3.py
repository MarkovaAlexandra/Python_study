# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int
import random
my_list = []
for i in range(6):
    my_list.append(random.randint(0,30))
print(my_list)
for i in range(6):
    k = random.randint(0,5)
    l = random.randint(0,5)
    my_list[k], my_list[l] = my_list[l], my_list[k]
print(my_list)