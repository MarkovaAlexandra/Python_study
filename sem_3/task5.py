# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
my_ex_list = [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введите число = '))
my_list1 = [0,1]
for i in range(2,num+1):
    my_list1.append(my_list1[i-2]+my_list1[i-1])
print(my_list1)
my_list2 = [0,1]
for i in range(2,num+1):
    my_list2.append(my_list2[i-2] - my_list2[i-1])
print(my_list2)
my_list2 = my_list2[::-1]
my_list2.remove(0)
negafibonacci = my_list2 + my_list1
print(negafibonacci)