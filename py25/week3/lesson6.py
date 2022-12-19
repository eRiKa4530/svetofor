# Лекцияю Области видимости и пространство имен

# LEGB:  
   # L - Local
   # E - Enclosed
   # G - Global
   # B - build-in

# import this
# x = 'Это глобальное переменная'
# def func1():
#     x = ' Это замкнутая переменная'
#     def func2():
#         x = ' Это локальное переменная'
# func1()    

# x = 2 # Это глобальная

# def func1(x):
#     x +=2 #Это локальная
#     return x 
# print(x)    
# print(func1(x))
# print(x)

# x = 0 
# def counter():
#     global x 
#     x = x +1
# print(x)  # 0  
# counter() # 1
# counter() # 2
# counter() # 3
# print(x) # 3

# def func2():
#     global x
#     x = 3
# print(x) # Error    
# func2()    
# print(x)   # 3  

# def func1():
#     x = 2
#     def func2():
#         nonlocal x 
#         x = x + 1
#         print(x)
#     func2()
# func1()    

# x = 2
# def func1():
#     x = 3
# func1()    

# print(globals())

# x = 'Я глобальная переменная!'
# def my_func():
#     x = 'Я могу изменяться,'
# my_func()    
# print(x)

# a = 2
# def func1():
#     global a
#     a = 3
#     a = a+3

#     def func2():
#         global a
#         #a = 4
#         print(a)
#     func2()
# func1()        
 
# x = 2
# print( x is globals()['x']) # True

# print(dir(__builtins__))

# import math
# print(math.pi)
# def func1():
#     PermissionError(math.pi)
# func1    


# def f1 ():
#     x = None
#     def f2():
#         nonlocal x
#         x = 2+8
#     f2()
#     print(x)
# f1() 
# print() 

# from math import pi
# print(round(pi,2))


# for i in [1,2,3]: # циклы и операторы область видимости не создает
#     x = i
# print(i)
# print(x)

# a = 2
# def func1():
#     global a
#     a += 3
# def func2():
#     nonlocal a
#     a += 4
#     func2()
#     print(a)
# func1() 
# print(a)  

def get_salary(amount):
  global balance
  balance += amount
def pay_bills(amount, log_name):
    global balance
    balance -= amount
    print(f'Вы заплатили{amount} сом за {log_name}') 
def get_balance():
    global balance
    print(f'У вас на счету {balance} сом')   
get_salary(1000)
get_balance()
pay_bills(400, 'кабельное тв')
get_balance()