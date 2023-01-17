from random import randint as RI
import time
print()
print('            Привет! Играем в крестики нолики')
print('Чтобы походить, надо будет ввести номер строки (1-2-3 сверху вниз)', 'и номер столбца (1-2-3 слева направо)', sep='\n')
print('ПОЛЕ')

pole = [['-']*3 for i in range(3)]
for i in range(3):
    for j in range(3):
        print(pole[i][j],end=' ')
    print()
print()
player1 = 'bot'
player2 = input('Введи свое имя = ')
print(f'Первый ход определим жеребьевкой, если выпадет число 1 - первым ходит {player1}, если 2 - {player2}')
lottery = RI(1,2)
print(f'выпало {lottery}')

if lottery == 1:
    first = player1
    second = player2
else:
    first = player2
    second = player1


while True:
    if first == player1:
        print(f'ходит {player1}')

        row = RI(0,2)
        col = RI(0,2)
        while pole[row][col] == 'x' or pole[row][col] == '0':
            row = RI(0,2)
            col = RI(0,2)
        pole[row][col] = '0'
        time.sleep(1)  
        for i in range(3):
            for j in range(3):
                print(pole[i][j],end=' ')
            print()

        flag = False
        for i in range(3):
            if pole[i][0]==pole[i][1]==pole[i][2] != '-':
                flag = True
        for j in range(3):
            if pole[0][j]==pole[1][j]==pole[2][j] != '-':
                flag = True


        if pole[0][0]==pole[1][1]==pole[2][2] != '-':
            flag = True
        if pole[0][2]==pole[1][1]==pole[2][0] != '-':
            flag = True
        if flag == True:
            print(f'Победил {player1}')
            break
    

        print(f'ходит {player2}') 
        row_try = input('введите номер строки = ')
            
        col_try = input('введите номер столбца = ')

        while  not col_try.isdigit() or not row_try.isdigit() or int(row_try) <= 0 or int(col_try) <= 0 or int(row_try) > 3 or  int(col_try) > 3 or pole[int(row_try)-1][int(col_try)-1] != '-':
            print('попробуй еще раз')
            row_try = input('введите номер строки = ')
            col_try = input('введите номер столбца = ')
        else:
            row = int(row_try)-1
            col = int(col_try)-1
            pole[row][col]='x'
            time.sleep(1)  
            for i in range(3):
                for j in range(3):
                    print(pole[i][j],end=' ')
                print()
        print()

        flag = False
        for i in range(3):
            if pole[i][0]==pole[i][1]==pole[i][2] != '-':
                flag = True
        for j in range(3):
            if pole[0][j]==pole[1][j]==pole[2][j] != '-':
                flag = True

        if pole[0][0]==pole[1][1]==pole[2][2] != '-':
            flag = True
            
        if pole[0][2]==pole[1][1]==pole[2][0] != '-':
            flag = True
        if flag ==True:
            print(f'Победил {player2}')
            break

    if first == player2:
        print(f'ходит {player2}')

        row_try = input('введите номер строки = ')
            
        col_try = input('введите номер столбца = ')

        while  not col_try.isdigit() or not row_try.isdigit() or int(row_try) <= 0 or int(col_try) <= 0 or int(row_try) > 3 or  int(col_try) > 3 or pole[int(row_try)-1][int(col_try)-1] != '-':
            print('попробуй еще раз')
            row_try = input('введите номер строки = ')
            col_try = input('введите номер столбца = ')
        else:
            row = int(row_try)-1
            col = int(col_try)-1
            

            pole[row][col]='x'
            time.sleep(1)  
            for i in range(3):
                for j in range(3):
                    print(pole[i][j],end=' ')
                print()
        print()

        flag = False
        for i in range(3):
            if pole[i][0]==pole[i][1]==pole[i][2] != '-':
                flag = True
        for j in range(3):
            if pole[0][j]==pole[1][j]==pole[2][j] != '-':
                flag = True


        if pole[0][0]==pole[1][1]==pole[2][2] != '-':
            flag = True
        if pole[0][2]==pole[1][1]==pole[2][0] != '-':
            flag = True
        if flag == True:
            print(f'Победил {player2}')
            break

        print(f'ходит {player1}')

        row = RI(0,2)
        col = RI(0,2)
        while pole[row][col] == 'x' or pole[row][col] == '0':
            row = RI(0,2)
            col = RI(0,2)
        pole[row][col] = '0'
        time.sleep(1)  
        for i in range(3):
            for j in range(3):
                print(pole[i][j],end=' ')
            print()


        
        flag = False
        for i in range(3):
            if pole[i][0]==pole[i][1]==pole[i][2] != '-':
                flag = True
        for j in range(3):
            if pole[0][j]==pole[1][j]==pole[2][j] != '-':
                flag = True


        if pole[0][0]==pole[1][1]==pole[2][2] != '-':
            flag = True
        if pole[0][2]==pole[1][1]==pole[2][0] != '-':
            flag = True
        if flag == True:
            print(f'Победил {player1}')
            break


