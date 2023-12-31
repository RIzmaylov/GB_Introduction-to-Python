from logger import *
from date_create import *
from copying import *

def interface():
    with open('Seminar_04_2\phonebook.txt', 'a'):
        pass

    command = -1
    while command != '5':
        print('Выберите вариант взаимодействия:\n'
            '1. Добавить контакт\n'
            '2. Вывести справочник\n'
            '3. Поиск контакта\n'
            '4. Копирование контакта\n'
            '5. Выход из программы')
        print()
        command = input('Введите номер команды: ')

        while command not in ('1', '2', '3', '4', '5'):
            print('Введите корректный номер меню!')
            command = input('Введите номер команды: ')

        match command:
            case '1':
                add_contact(create_contact())
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                copying_contact()
            case '5':
                print('Всего хорошего!')
