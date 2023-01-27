journal = {}
path = '3а.txt'
predm = ''
pupil = ''
students = []
predmets = []
students_dicts = []
pupils = []




def open_journal(path):
    global journal
 
    with open(path, 'r',encoding="UTF-8") as file:
        data = file.readlines()

    for line in data:
        predm = (line.strip().split('-')[0])           #по дефису режем каждую линию, на предмет и отальное                   
        predmets.append(predm)                         #предметы складываем в список predmets
        pupil = line.strip().split('-')[1]             
        students.append(pupil)                         #остальное складываем в список students

    for pupil in students:                             #разделим в студентах по ; 
        element = pupil.split(';')
        pupil_dic = {}                                 # для каждого студента свой словарь 
        for j in element:
            pupils.append(j.split(':')[0])
            pupil_dic[j.split(':')[0]] = (j.split(':')[1]).split(',') # делим по : фамилия ключ, оценки сплитим по , в список
        students_dicts.append(pupil_dic)               # добавляем словарь в список словарей
   
    # print(f'predmets {predmets}')
    # print(f'students{students}')
    # print(f'students_dicts{students_dicts}')
    # print(f'pupils {pupils}')
  
    journal = dict(zip(predmets,students_dicts))         # zip список предметов со списком словарей (студент: список оценок)
    return predm, journal

def get_journal():
    global journal
    return journal

def get_predmets():
    global predmets
    return predmets

def get_pupils():
    global pupils
    return pupils


def provesti_urok(predmet,uchenik,ocenka):
    for key in journal.keys():
        if key == predmet:
            for k in (journal[key]).keys():
                if k == uchenik:
                    (journal[key][k]).append(ocenka)
    
def save_journal():
    global journal
    data = []
    for key in journal.keys():
        line = key + '-'
        for key, value in journal[key].items():
            line = line + key + ':' + (','.join(value)) +';'
        line=line[:-1]
        # print(line)
        data.append(line)
    with open(path,'w',encoding='UTF-8') as file:
        data = file.write('\n'.join(data))
    print('Данные сохранены')
    