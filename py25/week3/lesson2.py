"""
Обработка исключений. Оператор try-except
НА случай когда мы хотим чтобы программа отлавливала
 какое-то исключение у нас есть оператор try-except.
Try (попытайся что - то сделать) except (блок кода которая обработывает искл.)


 Виды :
      - Ошибки
       -Исключения
"""
# Ошибки - проблема а синтаксисе( забывали двоеточие, 
# скобку , не сделали отступ,
#  неправильно назвали переменную  и тд.)
# 1)SynraxError -  забыли двоеточие, скобку,
#  неправильно назвали переменную и тд.
# 2f = 'hello'

# 2) IndentationError - неправильный отступ
#    aa = 2
# 3) TabError - неверная табуляция (смешивание пробелов и табов)

# 2. Исключения
# ZeroDivisionError (на ноль длить нельзя)
# print(2 / 0)
# num1 = int(input('num1:'))
# num2 = int(input('num2:'))

# try:
#     res = num1 / num2
#     print(res)
# except ZeroDivisionError:
#     print( 'НА ноль делить нельзя') 

# print('Конец!2')

#NameError
# print(z)
# try:
#     print(z)
# except NameError:
#     print(' Нет такой переменной!')

# TypeError - когда тип обьекта не подходт для операции
# name = input('Name:')
# age = int(input('Age:'))
# try:
#     print(name+''+age)
# except TypeError:
#     print('Не получиться!')    

# ValueError -  когда тип обьекта подходит для операции но не его значение
# try:
#     num1 = int(input('num1:'))
#     num2 = int(input('num2:'))
#     print(num1 + num2)
# except ValueError:
#     print('Введи число!')    
# IndexError-  такого индекса нет
# l = ['a','b']
# print(l[0])
# print[l(100)]

# KeyError - обращение к несуществующему ключу
# try:
#     dict_ = {'key1': 'value1', 'key2': 'value2'}
#     print()
# print(d['name'])
# except KeyError:
#      print('Нет такого ключа')
# ImportError - неправильный импорт
# from math import pi
# print(pi)
# ModuleNotFoundError -  не может найти модуль для импорта
# from math4867 import pi
# AttributeError-попйтаться вызвать несуществующий а
# трибут или метод у обьекта
# x = 2
# x.upper()

# KeyboardInterrupt - ctrl+c (прерывание процесса)
# while True:d = {'key': 2}
#     print('Hello')
# try:
#     print(2 / 0)
# except:
#     print('ошибка')    

# try: 
#     n1 = int(input('num1:'))
#     n2 = int(input('num2:'))
#     print(n1/n2)
# except:
#     print ('Ошибка')   



# try: 
#     n1 = int(input('num1:'))
#     n2 = int(input('num2:'))
#     print(n1/n2)
# except ( ZeroDivisionError,ValueError):
#     print ('Ошибка')   

# try: 
#     n1 = int(input('num1:'))try:    
#     string = ('kfhf')
#     num = 98
#     res_ = string+num
# except TypeError:
#      print('Unsupported option')
#     n2 = int(input('num2:'))
#     print(n1/n2)
# except Exception as e:
#     print ('Ошибка')   
#     print(e)
#     print(type(e))
# try: 
#     n1 = int(input('num1:'))
#     n2 = int(input('num2:'))
#     print(n1+n2) 
# # except ZeroDivisionError:     
#     print('На ноль делить нельзя')
# except  Exception:
#     print ('Я не что ты сделал но все таки обработала')
# except ValueError:  
#     print ('Вводите только число') 

# try: 
#     num1 = input(num1)
#     num1 = int(num1)
#     print(num1)
# except ValueError:
#     print('Введите число') 


# else: # когда в оброботке try не  врозникало исключуний
#     print('Все нормально вы вели число', num1)    
# finally: # выполняетсяв либом случае
#     print('Конец блока try-except')    

# age = int(input('Введите свой возраст:'))
# if age < 18:
# #     #raise Exception('вы слишком малы!') 
#     raise ValueError('Вы слишком малы!')
# else:
#     print('Все хорошо, проходи')
# # print('Hello')    
# b = 10
# c = 11
# try:
#     print(a) 
# except NameError: 
#     print("такого переменного не существует") 
#
# list_ = [1, 4, 9, 16, 25, 36] 
# try:
#     print(list_[5])
# except IndexError:
#     print('Нет такого элемента!')

# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# try:
#     print(dict_ {'key1'})
# except KeyError:
#     print('Нет такого ключа!')    


# try:
#     num1 = int(input("Введите число:")
#     num2 = int(input("Введите второе число:") 
#     res = num1 + num2
# else ValuError:
#   print('Введите только чило :')





# try:
#     num1 = int(input('Введите число:'))
#     num2 = int(input('Введите второе число:'))
#     res = num1/num2
# except ZeroDivisionError :
#      print('На ноль делить нельзя:') 
# except ValueError:
#      print('Вы не вели число')
# else:
#      print(res)    
# finally:
# #      print('Программа завершена!')   
# dict_ = {'key1': 'value1', 'key2': 'value2'} 
##################task8
# try:
#     num1 = int(input('Введите число:'))
#     num2 = int(input('Введите число:'))
#     res = num1/num2 
# except ZeroDivisionError:
#      print('На ноль делить нельзя')
#      print('Произошла ошибка') 

# try:
#      age = int(input('age:'))
#      if age < 18:
#           raise ZeroDivisionError('вы слишком малы')
#      else:
#           print('Добро пожаловать')
# except Exception as e:
#      print(type(e))          

# def func1()  :
#      print('hello world!')  
#      c = 2+2
#      return c
# a = func1()     
# print(a)    
# def func3(x, *args, **kwargs):
#      print(x)
#      print(args)#()
#      print(kwargs)#{k;v}  
# func3(4,2,[1,2,3,], name ='john')     
    

 
    
# cash = int(input(''))
# try:
#     if cash < 0:
#         print(cash)
# except ValueError:
#     print('Сумма не может быть отрицательной!')
   
# try:    
#     string = ('kfhf')
#     num = 98
#     res_ = string+num
# except TypeError:
#      print('Unsupported option')

# list_ = [1, 2, 3, 4]
# try:
#     for i in range(0, len(list_) + 1):
#        print(list_[i])
# except IndexError:
#      print
num = 23
num1 = 34
num2 = 57
print(num*num1)
res_ = num
