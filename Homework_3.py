#1. Використовуючи функцію print, надрукувати фразу “I love Python” 42 рази.
x = 'I love Python'
print(x*42)

#2. Створити змінну age_in_month, надавши їй значення вашого поточного віку в місяцях.
age_in_month = 334

#3. Створити змінну age_in_years, в яку записати ваш вік в роках на основі попередньої змінної.
#Підказка: використовуючи арифметичні оператори та/або приведення типів).
age_in_years = age_in_month//12
print(age_in_years)

#4. Створити змінну my_age, яка буде містити рядок “Му name is … I’m … years old”, де на замість пропусків буде підставлятись
#ваші імʼя та вік. Значення віку слід брати зі змінної age_in_years.
my_name = 'Vadym'
my_age = f'My name is {my_name}. I\'m {age_in_years}'
print (my_age)

#5. Створити змінну зі значенням 1. Використовуючи оператори порівняння, порівняти її із будь-якими іншими значеннями
#(мінімум 5 порівнянь) і перевірити вивід в інтерпретаторі.
q = 1
print(q > age_in_years)
print(q != age_in_month)
print (q >= 1)
print (q <= 0)
print (q == 1)
#6. Створити змінні a=2, b=5, c=6. На основі цих змінних створити змінну d, значення якої має бути “256”
#Формат здачі:
#прикріпити посилання на файли/папку у своєму репозиторії GitHub із виконаним домашнім завданням в LMS до даного уроку.
a=2
b=5
c=6
d = int(f'{str(a)}{str(b)}{str(c)}')
print(d)

