# Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
# Декоратор має працювати для різних функцій однаково.
import time
def my_decorator(func):
    def deco_func():
        print(time.strftime("%H:%M:%S"))
        func()
        print(func.__name__)
    return deco_func()

@my_decorator
def my_func():
    pass

# Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured".
class MyCustomException(Exception):
    pass
try:
  raise MyCustomException('Custom exception is occured')
except Exception as error:
  print(error)

# Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків дорівнює
# перед виконанням коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює.
# У випадку виникнення будь-якої помилки вона має бути надрукована текстом, проте програма не має завершити своєї роботи.
class CtxManager:
    def __init__(self,value):
        self.value=value
    def __enter__(self):
        print('==========')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('==========')

def printing():
    print('Printing in progress...')

with CtxManager(2) as call:
    printing()

# Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж, що і менеджер контексту із попереднього завдання.
def printing():
     print('Printing in progress...')
try:
    print('==========')
    printing()
except Exception as ex:
    print(str(ex))
else:
    print(f'The function {printing.__name__} is compete')
finally:
    print('==========')






