# Лекция : Логических выражения в Python. NoneType/ Условные операторы (if)

# boolean - неизменияемые тип данных
  # True  - истина
  # False - ложь

#  Логические операторы
# num1 = 2
# num2 = 3
# print(num1>num2) # False
# print(num1<num2) #True
# print(num1 >= num2) # False
# print(num1 <= num2) # true
# print(num1 == num2)# False
# print(num1 != num2) # True
# print(5 >= 5) #True

# s = "hello"
# print('e' in s) # True
# print('hello' in s) # True
# print('ol' in s) #False

# a = True #(1)
# b = False #(0)
# # print(a)
# # print(b)
# print(int(a)) # 1
# print(int(b))# 0
# print(bool(1000)) # True
# print(bool(-1))# True
# print(bool(0)) # False
# print(bool(0.1)) #True
# print(bool('he')) # True
# print(bool('')) # False

# and  и  or 
# print(True and True)
# print(2 > 3 and 2 > 3 ) #False and False
# name = ' John'
# age = 20 
# print(name == 'John' and age > 18) # True and True = True


# name = input('Введите ваше имя:')
# age = int (input('Введите вваш возраст:'))

# if age > 18 and  name == 'John':
#     print('Привет. Добро рожвловать! ')
#AND только тогда когда спрва и слева False или True
# print(True and True) # True
# print( True and False)# False
# print(False and True)# False
# print(False and False)# False
# OR  толко тогда когда хоть одна старна будет True
# print( True or True) # True
# print(True or False) # True
# print(False or True)# True
# print(False or False) # False

# print((True or True) and False) # False
# print(((False and False) or True) and (True or False)) # True and True == True

# print(not True) #False
# print(not False) # True

# a = 18

# if a > 18:
#     print('Привет')
# else:
#      print('Как тебя зовут?')    


# num2 = inr(input('Ведите число num2:'))
# num2 = int(input('Введите число num2'))

# operator = input('Выберите оператор: +, -,*,/ :')
# if operator == '+':
#     print(num1 + num2)
# if operator == '-' :
#     print(num1 - num2)
# if operator == '*':
#     print(num1 * num2)
# if operator == '/':
#     print(num1 / num2)

# if operator == '+':
#     print(num1 + num2)
# elif operator == '-' :
#     print(num1 - num2)
# elif operator == '*':
#     print(num1 * num2)
# elif operator == '/':
#      print(num1 / num2)
# else:
#     print('Нет такого оператора')

# age = 40 
# name = 'John'

# if age == 40 and name == 'John' :
#     print('Привет ты админ!')
# # if name == 'John':    
# #      print('Привет John ты не админ')
# elif name == 'John':    
#     print('Привет John ты не админ')

# num = 3 

# if num % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное') 

# Тернорное операторы  
# print('Hello') if True else print('Goodbuy')
# num1 = 5
# num2 = 4
# print(num1) if  num1 > num2 else print(num2)

# res = 'John' if False else 'Sam'
# print(res)

#Моржовое оператор (с Python 3.8)
# n = 5
# print(n)

# print(n := 5)
# print(c := 3)

#полендромные слова
# s = input('Ввыведите строку:')
# if s == s[::-1] :
#     print('YES')
# else:
#     print('No')

# NoneType - (Ничего)
# age = None 
# print(type(age))



# Task  1

# password = input('Введите пароль:')

# if password.isdigit() and len(password ) >= 8:
#   print('Ваш пароль сохранен')

# if not password.isdigit():
#   print('Ваш пароль должен хранить только числа')

# if not len(password) >= 8:
#   print('Ваш пароль должен содержать не менее 8 символов')

# Задачка 2

# point = input('Введите свои баллы по математике, английскому языку и литературе через запятую:').split(', ')
# math = int(point[0])
# english = int(point[1])
# litr = int (point[-1])
# # print(math , english,litr)
# average = (math + english +litr) / 3

# if average > 69:
#   print( f'Вы допущены к экзаменом . Ваш средний балл составляет{round(average , 1)}')
# else :
#   print('ВЫ не допущены к экзаменом')  

# Задачка 3 
# import random
# play = ['Камень', 'Ножнецы', 'Бумага']
# my_choice = input('Ваш выбор: ')
# computer_choice = random.choice(play)

# print(my_choice)
# print(computer_choice)

# if my_choice == 'Ножницы' and computer_choice == 'Бумага':
#   print(f' Выбор компьютера: {computer_choice}\n Вы выиграли')
# elif my_choice == 'Ножницы' and computer_choice == 'Камень':
#   print(f' Выбор компьютера: {computer_choice}\n Вы проиграли')
# elif my_choice == 'Камень' and computer_choice == 'Ножнецы':
#   print(f' Выбор компьютера: {computer_choice}\n Вы выиграли')
# elif my_choice == 'Камень' and computer_choice == 'Бумага':
#   print(f' Выбор компьютера: {computer_choice}\n Вы проиграли')
# elif my_choice == 'Бумага' and computer_choice == 'Камень':
#   print(f' Выбор компьютера: {computer_choice}\n Вы выиграли')
# elif my_choice == 'Бумага' and computer_choice == 'Ножницы':
#   print(f' Выбор компьютера: {computer_choice}\n Вы проиграли')
# elif my_choice == ('Бумага' and computer_choice == 'Бумага') or my_choice == ('Камень' and computer_choice == 'Камень') or my_choice == ('Бумага' and computer_choice == 'Бумага'):
#   print(f' Выбор компьютера: {computer_choice}\n Ничья')



# inp1 = 2 
# inp2 = 3
# inp3 = 4
# print(inp1 * inp1)
# print(inp2 * inp2)
# print(inp3 % inp3)
# num1 = 2
# num2 = 4
# # num3 = 2.5
# print(num1 % num2)
# print(num3 * 2)
# a = 12 / 4
# b = 12 // 4 
# c = 12 % 4
# print(a,b,c)
# day = 365
# mart = 12
# y = 7
# print((mart*y) * day)
