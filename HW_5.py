# 1. Створити програму, яка буде очікувати від користувача введення тексту і виведе інформацію по кожному надрукованому символу:
# це “число” + яке воно (парне, непарне),
# це “буква” + яка вона (велика чи маленька),
# це “символ”
#
def symbol_checker():
    enter = input("Enter your text ")
    count = len(enter)
    for x in enter:
        if x.isdigit():
            if int(x) % 2 == 0:
                print(f'{x} is even')
            elif int(x) % 2 != 0:
                print(f'{x} is odd')
        elif x.isalpha():
            if x.isupper():
                print(f'{x} Bigdaddy letter')
            elif x.islower():
                print(f'{x} small letter')
        else:
            print(f'{x} symbol')
symbol_checker()

# 2. Створити програму, яка буде друкувати в консоль “I love Python” кожні 4.2 секунди, поки її виконання не буде перервано вручну.
# Підказка: для того, щоб програма могла зупинитися на вказаний час, можна використати бібліотеку time (import time), а саме функцію sleep().
# (time.sleep(second), де second, це кількість секунд, які програма має чекати).

import time as time
def love():
    while True:
        time.sleep(4.2)
        print ('I love Python')
love()
