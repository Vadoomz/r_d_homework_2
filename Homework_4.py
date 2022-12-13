#1. Створити програму, яка буде очікувати введення тексту від користувача і повідомляти —
#чи є введений текст “числом” чи “словом”.
#2. Якщо введений текст “число”, програма має також вказати чи є воно парним чи непарним.
#3. Якщо це “слово”, програма має вказати його довжину.

def type_checker():
    enter = input("Enter your text ")
    if(enter.isdigit() == True):
        if (int(enter) % 2 == 0):
            print('Your enter is even number')
        elif (int(enter) % 2 != 0):
            print('Your enter is odd number')
    else:
        print(f'Your enter is text {len(enter)} symbols long')
type_checker()