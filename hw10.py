# 1. До завдання, в якому ви реалізовували телефонну книгу, додати валідацію номера телефону за допомогою RegEx.
# Врахувати можливість декількох форматів: +380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX
import json
import re
enter = input('''You can see all contacts(stats), all names(list), someone\'s number(show) or (add), (delete) contacts.
Enter your command: ''')
if enter == 'add':
    name = input('Enter name to add: ')
    phone = input('Enter phone to add: ')
    match1 = re.search('\+380\d{9}', phone)
    match2 = re.search('380\d{9}', phone)
    match3 = re.search('0\d{9}', phone)
    try:
        if match1:
            m = match1[0]
        elif match2:
            m = match2[0]
        elif match3:
            m = match3[0]
        with open('Newj.JSON', 'r+') as handle:
            js = json.load(handle)
            phone_record = js.setdefault(name, m)
        with open('Newj.JSON', 'w') as f:
            json.dump(js, f)
    except:
        print('You try to enter invalid number. Try again')
    else:
        print(f'Name {name} successfully added with number {m}')
elif enter == 'stats':
    with open('Newj.JSON', 'r+') as handle:
        js = json.load(handle)
        print(js.values())
elif enter == 'delete':
    delete = input('Enter name you want to delete: ')
    with open('Newj.JSON', 'r+') as handle:
        js = json.load(handle)
    if delete in js:
        del js[delete]
        with open('Newj.JSON','w') as f:
            json.dump(js, f)
        print(f'Contact {delete} was successfully deleted')
    else:
        print('Sorry, there is no such contact here')
elif enter == 'list':
    with open('Newj.JSON', 'r+') as handle:
        js = json.load(handle)
    print(js.keys())
elif enter == 'show':
    show = input('Find your contact by name: ')
    with open('Newj.JSON', 'r+') as handle:
        js = json.load(handle)
    print(js.get(show, 'Sorry, there is no such contact here'))
else:
    print('You entered something unexpected. Try again')