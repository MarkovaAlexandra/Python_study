# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
import random
import time

print()
print()
print('Давайте сыграем в игру "Последняя конфета"')
print('Правила такие: вы по очереди берете конфеты со стола, не меньше 1, но не больше 28')
print('Тот, кто сделает последний ход(заберет последнюю конфету), получает все')
player_1 = input('Введите имя первого игрока = ')
player_2 = input('Введите имя второго игрока = ')
candies = int(input('введите количество конфет = '))
print(f'Первый ход определим жеребьевкой, если выпадет число 1 - первым ходит {player_1}, если 2 - {player_2}')
lottery = random.randint(1,2)

if lottery == 1:
    first = player_1
    second = player_2
else:
    first = player_2
    second = player_1
print(f'Выпало число {lottery}, первый ход достается  {first}')
print(f'{first}, возьми конфеты ')


while candies > 1:
    
    take_first_try = input('Сколько конфет вы берете = ')
    while not take_first_try.isdigit() or int(take_first_try) < 1 or int(take_first_try) > 28 or int(take_first_try) > candies:
        print('     ХОД НЕВЕРНЫЙ','Возьмите не меньше от 1 до 28 конфет, но не больше, чем на столе', sep ='\n')
        take_first_try = input('Сколько конфет вы берете = ')
    else:
        take_first = int(take_first_try)
    candies = candies - take_first
    if candies == 0:
        print(f'!!! УРА !!! УРА !!! УРА!!! Победил {first}')
    else:
        time.sleep(1)
        print(f' на столе осталось {candies} конфет, ход переходит к {second}')
    take_second_try = input('Сколько конфет вы берете = ')
    while not take_second_try.isdigit() or int(take_second_try) < 1 or int(take_second_try) > 28 or int(take_second_try) > candies:
        print('     ХОД НЕВЕРНЫЙ','Возьмите не меньше от 1 до 28 конфет, но не больше, чем на столе', sep ='\n')
        take_second_try = input('Сколько конфет вы берете = ')
    else:
        take_second = int(take_second_try)
    candies = candies - take_second
    if candies == 0:
        print(f'!!! УРА !!! УРА !!! УРА!!! Победил {second}')
    else:
        time.sleep(1)
        print(f' на столе осталось {candies} конфет, ход переходит к {first}')

