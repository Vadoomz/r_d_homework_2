# 1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.
import json
enter = input('''You can see all contacts(stats), all names(list), someone\'s number(show) or (add), (delete) contacts.
Enter your command: ''')
if enter == 'add':
  name = input('Enter name to add: ')
  phone = input('Enter phone to add: ')
  with open('Newj.JSON','r+') as handle:
    js = json.load(handle)
    phone_record = js.setdefault(name, phone)
  with open('Newj.JSON','w') as f:
      json.dump(js, f)
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
# Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
# При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
# Підказка: Ви можете використати бібліотеку json, яка допоможе із перетворенням dict в JSON string (при записі в файл)
# і JSON string в dict (при читанні із файлу). Файл слід оновлювати після кожної успішної операції add або delete.
#
# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.
#
# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.
class MyCustomException(Exception):
    pass
try:
  raise MyCustomException('Custom exception is occured')
except Exception as error:
  print(error)