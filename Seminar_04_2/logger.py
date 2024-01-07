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
