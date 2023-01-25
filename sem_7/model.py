phone_book = {}
keys = []
values = []
path = 'base.txt'

def get_phone_book():
    global phone_book
    return phone_book


def open_phone_book():
    global phone_book
    global path
    with open(path,'r',encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            values.append(line.strip().split(';'))
        for i in range(len(values)):
            keys.append(i+1)
        phone_book = dict(zip(keys,values))

def update_phone_book(contact: list):
    global phone_book
    phone_book[len(phone_book)+1]=contact

def save_phone_book():
    global phone_book
    global path
    data = []
    for value in phone_book.values():
       data.append(';'.join(value))
    with open(path,'w',encoding='UTF-8') as file:
        data = file.write('\n'.join(data))

def search_contact(search: str):
    global phone_book
    search_results = {}
    for value in phone_book.values():
        for i in range(len(value)):
            if search in value[i].lower():
                for k in phone_book.keys():
                    if phone_book[k]==value:
                        search_results[k] = value
    return search_results

def changing_contact(changed: list):
    global phone_book
    for k in phone_book.keys():
        if k == int(changed[0]):
            new_data = phone_book.get(k)
            # print(new_data)
            new_data[changed[1]-1]=changed[2]
            # print(new_data)
            phone_book[k]=new_data
   
def deleting_contact(key_to_delete):
    global phone_book
    for k in phone_book.keys():
        if k == key_to_delete:
            del phone_book[k]
            break


            