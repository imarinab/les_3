# Присвоение значений для переменных и замена значений местами
a = 10
b = 14
a, b = b, a
a
    14
b
    10

# Функция Inpit
age = input ('How old are you?')
    How old are you?>? 25
print (f'You was born in {2022-int(age)} year')
    You was born in 1997 year

# Функция Type
type (age)
    <class 'str'>

# Функция Isinstance
isinstance(age, int)
    False
isinstance(age, str)
    True
isinstance(age, (int, str))
    True

#Привидение к другим типам
bool (0)
    False
bool(1)
    True
bool ('0')
    True
bool('')
    False
int (True)
    1
int (False)
    0
int (8.7)
    8
int (4.5)
    4
int ('123')
    123
int('123.89')
    ValueError: invalid literal for int() with base 10: '123.89'

# Округление
round(7.5)
    8
round (2.5)
    2

# Строки, объединие строк
a = 'Hello'
b = 'World'
c = a + ' ' + b
print (c)
    Hello World

d = (a + ' ') * 5
d
    'Hello Hello Hello Hello Hello '

f = a[0]
f
    'H'

c
    'Hello World'
c[:]
    'Hello World'
c[6:]
    'World'
c[:6]
    'Hello '

len(c)
11

# Форматирование строк
name = 'Álex'
age = 28
"Hello, My name is {}. I'm {} years old".format(name, age)
    "Hello, My name is Álex. I'm 28 years old"

f"Hello, My name is {name}. I'm {age} years old"
    "Hello, My name is Álex. I'm 28 years old"

# Разделение и объединение
numbers = 'one, two, three'
numbers.split(',')
    ['one', ' two', ' three']

numbers = 'one, two, three'
f'{numbers + ","} four'
    'one, two, three, four'

# Регистр
c
    'Hello World'
c.upper()
    'HELLO WORLD'
c.lower()
    'hello world'
c.capitalize()
    'Hello world'
c.swapcase()
    'hELLO wORLD'
c.title()
    'Hello World'
