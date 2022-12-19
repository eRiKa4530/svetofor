# Тип данных: str (строки)
# Строка в Python - это последовательный набор символов, который может состоять как из цифр так и из букв и разделителей

# Строки это неизменяемый, упорядоченный, индексируемый тип данных

# name = 'John'
# print(id(name))
# name = "John2"
# print(id(name))
# name = """John3"""
# print(id(name))

# text = 'Hello world'
# print(text)

# s = 'hey dsad asd asd asd asd asd sad'
# print(s[0])
# print(s[-1])
# print(s[-3])

# s = 'hello'
# print(s[0:2]) # he
# print(s[1:5])  # ello
# print(s[1:]) # ello
# print(s[:3])  # hel
# print(s[:]) # hello
# print(s[0::2]) # hlo
# print(s[::3]) # hl
# print(s[::-1]) # olleh

# s = 'jhcfbdsj kfhdsjkfha kjsdfh ajkfh d'
# print(len(s)) # 34

# name = 'John'
# surname = 'Snow'
# full_name = name + " " + surname # Конкатенация (сложение строк)
# print(full_name)

# print('hello' + 'world' + str(2))
# print('h' + 2) # ERROR

# name = input('Введите ваше имя: ')
# age = int(input('Введи свой возраст: '))
# # print(type(name))
# # print(type(age))
# # print("Привет тебя зовут", name, 'тебе', age, 'лет')
# print(f'Привет тебя зовут {name} тебе {age} лет') # интерполяция строк (форматирование строк) (f-строки)

# экранированные последовательности - это последовательности, которые начинаются с символа \ за которым следует один или более символов

# print('Hello\nJohn')
# print('Hello\tJohn')
# print('Hello\n\tJohn')
# print('Hello\\')
# s = 'h\n\nJohn'
# print(s)
# print('hello\raa')
# print('Hello \\')
# print('I\'am John')
# print('hello "JOHN"')
# print("hello 'JOHN'")
# print(r'hello\nworld')
# print('a' in 'Sam')
# print('o' in 'Sam')
# print('j' in 'John')
# print('hn' in 'John')


# print(dir(str))
# print(dir('hhh'))

# Методы строк: 

# s = 'Hello John'
# print(s.isdigit())  # Состоит ли строка только из цифр
# print(s.isalpha())  # только из букв
# print(s.isalnum())  # только из цифр или букв
# print(s.islower())  # находится ли вся строка в нижнем регистре
# print(s.isupper())  # в верхнем 
# print(s.isspace())  # состоит ли строка из неотображаемых символов (пробел, экранированные последовательности)
# print(s.istitle())  # Начинаются ли слова с заглавной буквы

# s = 'hello'
# s = s.replace('e', 'a')
# s = s.replace('llo', 'a')
# s = s.replace('l', 'h', 1)
# s = s.replace('l', '')
# print(s)

# s = 'Hello John my name is Sam'
# # s = s.split(' ')
# s = s.split('o')
# print(s)

# s = 'John'
# print(s.upper())
# print(s)

# print('aADSDsads'.lower())

# s = 'helLo johN'
# print(s.title())
# print(s.swapcase())
# print(s.capitalize())

# s = 'asdkjhasashdg kash dk '
# print(s.count('a'))
# print(s.count(' '))
# print(s.count('dk'))

# strip, startwith, endwith, join, ord, chr


# strip,startwith, endwith, join ord, chr

# email = 'admin@gmail.com'
# # print(email.endswith('@gmail.com'))
# # print(email.endswith('.ru'))
# print(email.startswith('admin'))
# print(email.startswith('test'))
# print(email.startswith("admin2")) #false

# s ="    hello  world     "
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# s = 

# s = '#he#she#they#it'
# l = s.split("#")
# print(l)



# print(ord('a')) #уникальное значение каждого символов
# print(ord("d")) 

# print(chr(97))
# print(chr(98))

# x = 2
# print(id(x))
# x = x + 2
# print(id(x))

# name = 'Joffrey'
# greeting = 'Hello'
# print(f'{greeting} {name}')
