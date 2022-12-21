# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
my_list = [1.1, 1.2, 3.1, 5, 10.01]
def Diff_Max_Min_Float (list):


    my_new_list = []
    for i in range(len(list)):
        my_new_list.append(round((list[i]-int(list[i])),4))
    my_new_list.remove(0)
    maximum = max(my_new_list)
    minimum = min(my_new_list)
    result = maximum-minimum
    return result

my_list = [1.1, 1.9, 3.1, 6.048, 5, 10.001] 
print(f'{my_list} => {Diff_Max_Min_Float(my_list)}')


