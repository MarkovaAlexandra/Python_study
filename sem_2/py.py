# 1. Напишите программу, которая принимает на вход число N 
# и выдаёт последовательность из N членов.

# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81
num = 5
el = 1
# for i in range(num-1):
#     print(el*-3)
#     el=el*-3
# my_list = []
# my_list.append(1)
# i = 1
# for i in range(num-1):
#     my_list.append(el*-3)
#     el = el*-3
# print(*my_list)

# Стоун (Кирилл): 2. Для натурального n создать словарь ключ-значение,
# состоящий из элементов последовательности 3n + 1.

# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} 
# my_dict = {}
# for i in range(1,7):
#     my_dict[i] = 3*i + 1
# print(my_dict)

# text = 'кукушка кукушонку купила капюшон'
# string = 'ка'
# print(text.count(string))

a = input()
b = input()
c = input()
lengtha = len(a)
lengthb = len(b)
lengthc = len(c)
my_list = [lengtha, lengthb, lengthc]
print(my_list)
my_list.sort()
print(my_list)
if my_list[2] - my_list[1] == my_list[1] - my_list[0]:
    print('YES')