# 1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.
import json
try:
    with open('Newj.JSON', 'r+') as handle:
        phone_book = json.load(handle)
except:
    with open('Newj.JSON', 'w+') as handle:
        phone_book = {}
while True:
    enter = input('''You can see all contacts(stats), all names(list), someone\'s number(show) or (add), (delete) contacts.
    Enter your command: ''')
    if enter == 'add':
        name = input('Enter name to add: ')
        phone = input('Enter phone to add: ')
        phone_book.setdefault(name, phone)
        with open('Newj.JSON', 'w') as f:
            json.dump(phone_book, f)
    elif enter == 'stats':
            print(phone_book.values())
    elif enter == 'delete':
        delete = input('Enter name you want to delete: ')
        if delete in phone_book:
            del phone_book[delete]
            with open('Newj.JSON', 'w') as f:
                json.dump(phone_book, f)
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
# Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
# При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
# Підказка: Ви можете використати бібліотеку json, яка допоможе із перетворенням dict в JSON string (при записі в файл)
# і JSON string в dict (при читанні із файлу). Файл слід оновлювати після кожної успішної операції add або delete.
#
# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.
# import time
# def my_decorator(func):
#     def deco_func(*args, **kwargs):
#         f = func(*args, **kwargs)
#         with open('New_txt.TXT', 'a+') as file:
#             n = func.__name__
#             t = time.strftime("%H:%M:%S")
#             note = f'Time of call function, {n}, is, {t}'
#             file.write(note+'\n')
#         return f
#     return deco_func
# @my_decorator
# def my_func(par):
#   print(par**par)
# my_func(3)
# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.
# import time
# class MyCustomException(Exception):
#     def __init__(self, message = 'Custom exception is occured at '):
#         self.message = message
#         with open('error_file.TXT', 'a+') as erfile:
#             t = time.strftime("%H:%M:%S")
#             ertext = str(message + t + '\n')
#             erfile.write(ertext)
# try:
#     a=10/2
#     if a == 5:
#         raise MyCustomException
# except MyCustomException:
#     print("Check some error in file 'error_file.TXT'")
#

# with open('Newj.JSON', 'r') as file:
#     phone_book = json.load(file)
# name = input('Enter name to add: ')
# phone = input('Enter phone to add: ')
# phone_book.setdefault(name, phone)
# with open('Newj.JSON', 'w') as f:
#     json.dump(phone_book, f)