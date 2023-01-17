
import random
import time

print('Привет, я бот Матильда')
print('Давай сыграем в игру "Последняя конфета"')
print('Правила такие: мы по очереди берем конфеты со стола, не меньше 1, но не больше 28')
print('Тот, кто сделает последний ход(заберет последнюю конфету), получает все')


player_1 = input('Введи свое имя = ')
bot = 'Matilda'
candies = int(input('введите количество конфет = '))
print(f'Первый ход определим жеребьевкой, если выпадет число 1 - первым ходит {player_1}, если 2 - {bot}')
lottery = random.randint(1,2)


if lottery == 1:
    first = player_1
    second = bot
else:
    first = bot
    second = player_1

time.sleep(1)
print(f'Выпало число {lottery}, первый ход достается  {first}')

if second == bot:
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
    
            take_second = candies % 29
            if take_second == 0:
                take_second = candies % 28
            print(f'{second} берет {take_second} конфет')
        candies = candies - take_second
        if candies == 0:
            print(f'!!! УРА !!! УРА !!! УРА!!! Победил {second}')
        else:
            time.sleep(1)
            print(f' на столе осталось {candies} конфет, ход переходит к {first}')

if first == bot:
    while candies > 1:
    
        take_first = candies % 28
        if take_first==0:
            take_first = candies % 29
        print(f'{first} берет {take_first} конфет')
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
            
            
            
            