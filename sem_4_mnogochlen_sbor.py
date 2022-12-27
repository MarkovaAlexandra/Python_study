# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
stepen = int(input("Введите максимальную степень = "))
my_dict = {}                                             #задаю словарь {степень - коэффициент х}
for i in range(stepen, 0, -1):                           # циклом в ранже от макс степени до 1 по убыванию
    my_dict[i] = random.randint(-10,10)                  # у степени такой-то коэф х = рандом
# print(my_dict)
equation = ''                                            # сюда буда собирать строку с уравнением
for i in my_dict.items():
    if i[1] == 1:                                        # коэф 1 не печатаем
        equation = equation + (f'x^{i[0]} ')
    elif i[1] == -1:                                     # коэф -1 оставляем ток -
        equation = equation + (f'-x^{i[0]} ') 
    elif i[1] == 0:                                      # *0 остается 0, не печатаем ничего
        equation = equation

    else:
        equation = equation + (f'{i[1]}*x^{i[0]} ')      #значение * х в степени ключ пробел
# print(equation)
equation=equation.replace(' ',' + ').replace('+ -',' - ').replace('^1','')
# print(equation)
equation = equation[:-2]                                 # без последнего пробела и +
print(equation + '= 0')