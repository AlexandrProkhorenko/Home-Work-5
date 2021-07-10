
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


print('dgsfsg')
print('dfdfd')
print('sfgsfgsf')
print('sfgsfgsf')

def name():
    x = input('введите номер документа\n')
    for i in documents:
        if i.get('number') == x:
            print(i['name'])
            return



def number():
    number_document = input('Введите номер документа:\n ')
    for doc in directories:
        if number_document in directories.get(doc):
            print(f'Документ находиться на полке:'+ doc )
            return
    else:
        print(f"Документа с номером " + number_document + " не существует")
        return




def all_doc():
    for i in documents:
        c = i.get('type')
        b = i.get('number')
        m = i.get('name')
        print(c,b,m)



def add_documents():
    q = input('Укажите тип\n')
    a = input('Укажите номер\n')
    z = input('Укажите Имя\n')
    new_list = {}
    new_list['type'] = q
    new_list['number'] = a
    new_list['name'] = z
    documents.append(new_list)
    print('Добавлен новый документ', new_list)
    x = input('Укажите номер полки\n')
    if x in directories:
        directories[x].append(a)
        print(directories)
        return
    else:
        print('Ошибка ввода!')
        return




def delete_document():
    x = input('Введите номер документа который нужно удалить\n')
    for i in documents:
        if x in i.values():
            for i in list(documents):
                if x in i.values():
                    del (i['number'], i['type'], i['name'])
                    print('Элемент был удален')
            for g in directories.values():
                if x in g:
                    g.remove(x)
                    print('Элемент', x, 'был удален с полки')
            break
    else:
        print('Такого документа не существует')


def move_document():
    x = input('Укажите номер документа который нужно переместить\n')
    z = input('Укажите на какую полку его следует переместить\n')
    for i in documents:
        if x in i.values():
            print('Документ был найден')
            for elem in directories.values():
                if x in elem:
                    elem.remove(x)

            if z == '3':
                directories['3'].append(x)
                return (f'Документ был перенесен на полку:{z}')

            if z == '2':
                directories['2'].append(x)
                return (f'Документ был перенесен на полку:{z}')

            if z == '1':
                directories['1'].append(x)
                return (f'Документ был перенесен на полку:{z}')
    else:
        return ('Документ не был найден')







def add_sheld():
    ask_add = input('Вы хотите добавить новую полку? y/n\n')
    ask = input('Введите номер новой полки\n')
    if ask_add == 'y':
        if ask in directories:
            print('Такая полка уже существует!')
        else:
            directories[ask] = []
            print('Полка под номер',ask,'добавленна' )
            print(directories)
    else:
        print ('Завершение работы')




def start():
    while True:
        ask = input('Вы хотите начать работу или закончить ? y/n\n')
        if ask == 'y':
            p = input('Нажмите \'p\', что бы вывести имя человека\n'
                      'Нажмите\'s\', что бы вывести номер полки\n'
                      'Нажмите \'l\' что бы вывести весь список документов\n '
                      'Нажмите \'a\' что бы добавить новый документ\n'
                      'Нажмите \'d\' что бы добавить новый документ\n'
                      'Нажмите \'m\' что бы переместить документ на другую полку\n'
                      'Нажмите \'as\' что бы добавить новую полку в переччень\n')
            if p == 'p':
                name()
            elif p == 's':
                number()
            elif p == 'l':
                all_doc()
            elif p == 'a':
                add_documents()
            elif p == 'd':
                delete_document()
            elif p == 'm':
                move_document()
            elif p == 'as':
                add_sheld()
        elif ask == 'n':
            print('Выход из программы')
            break




start()































































