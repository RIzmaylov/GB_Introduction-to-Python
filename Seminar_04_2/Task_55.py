# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# Этапы работы:
# 1) Создать телефонный справочник:                 +++
#     - Открыть файл в режиме добавления (a)        +++
# 2) Добавить контакт:                              +++
#     - Запросить информацию у пользователя         +++
#     - Подготовить данные в необходимом формате    +++
#     - Открыть файл в режиме добавления (a)        +++
#     - Добавить контакт в файл                     +++
# 3) Вывести данные из файла на экран:              +++
#     - Открыть файл в режиме чтения (r)            +++
#     - Вывести информацию на экран                 +++
# 4) Поиск данных:                                  +++
#     - Запросить вариант поиска                    +++
#     - Запросить информацию у пользователя         +++
#     - Открыть файл для чтения (r)                 +++
#     - Сохранить данные в переменную               +++
#     - Осуществить поиск по файлу                  +++
#     - Вывести нужную информацию на экран          +++
# 5) Реализовать UI;                                +++
#     - Вывести варианты меню                       +++
#     - Получение запроса пользователя              +++
#     - Реализация запроса пользователя             +++
#     - Выход из программы                          +++

def input_name():
    return input('Введите имя: ')

def input_surname():
    return input('Введите фамилию: ')

def input_patronymic():
    return input('Введите отчество: ')

def input_phone():
    return input('Введите номер телефона: ')

def input_address():
    return input('Введите адрес: ')

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()

    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'

def add_contact(contact):
    with open('Seminar_04_2\phonebook.txt', 'a', encoding = 'UTF-8') as file:
        file.write(contact)

def show_info():
    with open('Seminar_04_2\phonebook.txt', 'r', encoding = 'UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        # print(file.read().rstrip())
        for n, contact in enumerate(contacts_list, 1):
            print(n, contact)


def search_contact():
    var_search = input('Выберите вариант поиска:\n'
                        '1. По фамилии\n'
                        '2. По имени\n'
                        '3. По отчеству\n'
                        '4. По телефону\n'
                        '5. По адресу\n')
    
    while var_search not in ('1', '2', '3', '4', '5'):
            print('Введите корректный вариант поиска!')
            var_search = input('Введите вариант поиска: ')

    index_var = int(var_search) - 1

    search = input('Введите данные для поиска: ')

    with open('Seminar_04_2\phonebook.txt', 'r', encoding = 'UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        if search in contact_lst[index_var]:
            print(contact_str)


def interface():
    with open('Seminar_04_2\phonebook.txt', 'a'):
        pass

    command = -1
    while command != '4':
        print('Выберите вариант взаимодействия:\n'
            '1. Добавить контакт\n'
            '2. Вывести справочник\n'
            '3. Поиск контакта\n'
            '4. Выход из программы')
        print()
        command = input('Введите номер команды: ')

        while command not in ('1', '2', '3', '4'):
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
                print('Всего хорошего!')
        
interface()