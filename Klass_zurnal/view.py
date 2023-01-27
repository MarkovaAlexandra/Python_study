
def main_menu():
    print('Введите номер класса: ')
    klass = input('класс = ')+'.txt'
    return klass

def save_and_exit():
    print(f'\tЕсли вы хотите сохранить журнал и выйти, введите "exit" \n\tвыйти без сохранения - "n" \n\tдля продолжения нажмите "enter"')
    user_choise = input('= ')
    return user_choise

def choose_lesson(lessons: list): 
    predmet_try = input('Какой урок провести? (для выхода введите exit)  = ')   
    while True:      
        if predmet_try == 'exit' or predmet_try == 'учше':
            predmet = predmet_try  
            break 
        else:
            if predmet_try not in lessons:
                print('Выберите из предметов в журнале')
                for lesson in lessons:
                    print(f'\t{lesson}')
                predmet_try = input('Какой урок провести? (для выхода введите exit)  = ')                   
            else:
                predmet = predmet_try
                break
    return predmet


def print_dict(journal):
    for key in journal.keys():
            print(f'{key}')
            for i,j in journal[key].items():
                print (f'\t {i}: {j}')  

def print_dict_lesson(journal,predmet):
    for key in journal.keys():
        if key == predmet:      
            print(key)
            for i,j in journal[predmet].items():
                print (f'\t {i}: {j}')


def choose_student(pupils: list):
    student_try =  input('Кто отвечает: (для выхода введите exit) = ')
    while True:
        if student_try == 'exit' or student_try == 'учше':
            student = student_try
            break
        else:                   
            if student_try not in pupils:
                print('Таких нет')
                student_try = input('Кто отвечает: (для выхода введите exit) = ')
            else:
                student = student_try
                break
    return student

def assessment():
    print('На что наотвечал: ')
    ocenka = input()
    if ocenka > '3':
        print('вот молодец')
    else:
        print('ну вот, а что скажет мама?')
    return ocenka