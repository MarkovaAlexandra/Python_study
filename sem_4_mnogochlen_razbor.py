# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]


# ПОШАГОВЫЙ РАЗБОР ДЛЯ ЧАСТНОГО СЛУЧАЯ
# equation  = '10* x^ 5 +   2*x^4 +    3*x^3 -2*x^2 - 5*x = 0'
# print(equation)
# equation = equation.replace(' ','')               #убрали пробелы
# print(equation)
# equation = equation.replace('+',',').replace('-',',-').replace('=0','').replace('x^','').replace('x','1')
# print(equation)
# equation = equation.split(',')                   # в список
# print(equation) 
# key = []                                         # сюда буду собирать ключи
# value = []                                       # сюда буду собирать значения
# for i in equation:
#     i = i.split('*')                             # разбей каждый элемент списка на список по сепаратору *
#     print(i)
#     key.append(int(i[1]))                        # 1 элемент получившегося подсписка положи в ключи
#     value.append(int(i[0]))                      # 0 положи в значения
# print(equation)
# print(key)
# print(value)
# my_dict = dict(zip(key,value))                   # собери словарь из списков(ключи, начения)
# print(my_dict)
# for i in range(1,10):                            # для каждого значения в ранже(0, макс степень)
#     print(my_dict.setdefault(i,0))               # вставь iый ключи со значением 0, если такого нет(если он дефолт)
# print(my_dict)                                   


# тут напишу функцию
def equation_parsing(string):
    string = string.replace(' ','').replace('+',',').replace('-',',-').replace('=0','').replace('x^','').replace('x','1')
    string = string.split(',')
    key = []
    value = []
    for i in string:
        i = i.split('*')
        key.append(int(i[1]))
        value.append(int(i[0]))
    my_dict = dict(zip(key,value))
    return(my_dict)

equation1 = '5*x^8 + 6*x^7 - 5*x^6+8*x^4-3*x^2   =0'
print(f'Первый многочлен = {equation1}')
equation2 = '7*x^8 -6*x^4  + 4*x^3 -x*2 = 0'
print(f'Второй многочлен = {equation2}')
dict1 = equation_parsing(equation1)
dict2 = equation_parsing(equation2)
print(f'коэффициенты и степени первого многочлена = {dict1}')
print(f'коэффициенты и степени второго многочлена = {dict2}')

result_key = set()                                          # создаем множество для запихания туда ключей из обоих словарей
for key in dict1:
    result_key.add(key)
for key in dict2:
    result_key.add(key)
print(f'множество ключей = {result_key}')
sum_equation = {}                                           # результирующий словарь
for key in result_key:                                      # возьми ключи из множества ключей 
    sum_equation[key] = dict1.get(key,0) + dict2.get(key,0) # и присвой им значение = сумма ??почему ключей, а не значений??
print(f'коэффициенты и степени суммы многочленов = {sum_equation}')

#собираем новый многочлен
def equation_get(dict={}):
    equation = ''
    for i in dict.items():
        equation = (equation + (f'{i[1]}*x^{i[0]} + ')).replace('+ -','- ')
        equation=equation[:-2] + '= 0'
    return(equation)

result=equation_get(sum_equation)
print(f'сумма многочлена = {result}')
