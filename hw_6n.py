# 1. Створити телефонну книгу, яка матиме наступні команди:
# stats: кількість записів
# add: додати запис
# delete <name>: видалити запис за іменем (ключем)
# list: список всіх імен в книзі
# show <name>: детальна інформація по імені
# Записи не мають повторюватися, заборонено перезаписувати записи, тільки видаляти і додавати заново.

phone_book = {'Vadym':'0665699589'}
while True:
    enter = input('''You can see all contacts(stats), all names(list), someone\'s number(show), (add) or (delete) contacts. 
    Enter your comand: ''')
    if enter == 'add':
        name = input('Enter name to add: ')
        phone = input('Enter phone to add: ')
        phone_book.setdefault(name, phone)
    elif enter == 'stats':
        print(len(phone_book))
    elif enter == 'delete':
        delete = input('Enter name you want to delete: ')
        if delete in phone_book:
            del phone_book[delete]
            print(f'Contact {delete} was successfully deleted')
        else:
            print('Sorry, there is no such contact here')
    elif enter == 'list':
        print(phone_book.keys())
    elif enter == 'show':
        show = input('Find your contact by name: ')
        print(phone_book.get(show, 'Sorry, there is no such contact here'))
    else:
        print('You entered something unexpected. Try again')
    print(phone_book.items())