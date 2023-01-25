

def main_menu():
    commands = ['Показать все контакты',
                'Открыть файл', 
                'Сохранить файл',
                'Новый контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Найти контакт',
                'Выйти из программы']
    print('Выберите пункт меню')
    for i in range(len(commands)):
        print(f'\t {i + 1} {commands[i]}')
    while True:
        try:
            user_input = int(input('Введите пункт меню:'))
            if user_input > 8 or user_input < 1:
                print(f'\t Такого пункта нет')
            if 0 < user_input < 9:
                break
            
        except ValueError:
            print(f'\t Введите цифрами')

    return user_input

def show_contacts(phone_book):
    if len(phone_book) > 0:
        # for item in phone_book:
        for key,value in phone_book.items(): 
            print(key, ':', *value)
   

    else:
        print('Телефонная книга пуста или не загружена')

def load_success():
    print('Телефоннаая книга загружена успешно')

def save_success():
    print('Телефоннаая книга сохранена успешно')

def partically_save_sucess():
    print('Готово')

def new_contact():
    name = input('Введите имя и фаилию нового контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def find_contact():
    find = input('Введите искомый контакт: ')
    return find

def change_contact(result):
    while True:
        try:
            key = int(input('Введите id контакта, который хотите изменить: '))
            if key  in result.keys():
                break
            if key not in result.keys():
                print(' id написан слева от контакта ')
        except ValueError:
            print('циферка слева от контакта')

    print('Какое поле будем менять: ')
    fields = ['Имя','телефон','комментарий']
    for i in range(len(fields)):
        print(f'\t{i+1}. {fields[i]}')
    while True:
        try:
            value_index_to_change = int(input('Введите номер поля: '))
            if value_index_to_change > 3 or value_index_to_change < 1:
                print(f'\t Такого пункта нет')
            if 0 < value_index_to_change < 4:
                break
            
        except ValueError:
            print(f'\t Введите цифрами')

    
    new = input('Новое поле: ')
    return  key,value_index_to_change,new

def delete_contact():
    key_to_del = int(input('Введите id контакта, который хотите удалить: '))
    return key_to_del
    