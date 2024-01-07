# План домашней работы:
# Сделать функционал копирования в отдельный файл:
#     1. Запрос названия нового файла у пользователя              +++
#     1.а. Функционал использования ранее введенного названия     +++
#     1.б. Тест корректности после введенного '!'                 +++
#     1.в. Тест корректности при введении сразу нового названия   +++
#     2. Запрос номера строки копирования                         +++
#     2.а. Проверка корректности введенных данных                 +++
#         Тесты: -1, -100, 0, 5, 100                              +++
#     3. Создание файла и копирование туда строки                 +++
#     3.а. Тест корректности копирования именно той строки        +++

name_file = ''

def copying_contact():
    global name_file
    temp_name_file = input('Введите название целевой телефонной книги или, если вы уже вводили его и хотите копировать данные в ту же книгу, введите - !: ')
    if temp_name_file == '!':
        if name_file == '':
            name_file = input('Название файла ранее введено не было, введите новое название: ')
        else:
            print(f'Вы копируете данные в телефонную книгу {name_file}\n')
    else:
        name_file = temp_name_file
            
    num_of_contact = int(input('Введите номер копируемой строки: '))


    with open('Seminar_04_2\phonebook.txt', 'r', encoding = 'UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        
    while num_of_contact > len(contacts_list) or num_of_contact <= 0:
        num_of_contact = int(input('Введите корректный номер копируемой строки: '))


    with open(f'Seminar_04_2\{name_file}.txt', 'a', encoding = 'UTF-8') as file:
        file.write(contacts_list[num_of_contact - 1] + '\n')

    print('Данные скопированы!\n')