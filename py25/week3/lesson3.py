"""
Введение  в функции. Позиционные и именнованные аргуметоы.
arg, kwargs. Аргументы по default.Аннотации функции

Встроенные функции: len , print,sum, max, min , int, str...

Функция  в Python = это обьект принемающийй аргументы и возвращающий значение
"""


# def info():
#     print('John')
#     print('Snow')
#     print('22 y.o')
# info()
# pass 
# info()
# pass
# info()
#!!!!!!! return - это возрат !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def my_sum( d,g): # Параметры
#     res = d+g
#     return res
# print(my_sum(3,5) )# Аргументы
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# num1 = int(input('num1:'))
# num2 = int(input('num2:'))
# def multy(x,y):
#     return x*y
# print(multy(num1,num2))   
# print(multy(2,4))

# def func1(s =7,s2 = 0):
#     return s+s2# поделфолту есть 2
# # print(func1(2,3))    # 5
# # print(func2('hello','John')) #helloJohn
# print(func1(2,3)) # 5
# print(func1(2)) #2
# print(func1()) # 7

#Аннотация функций

# def func2(x: str ,y: str) -> str:
#     r = x + y
#     # r = r +"john"
#     return r
# # print(func2(2,2))
# # print(func2([123], ['akj']))
# print(func2('h','w')) # функция работает тоолько со стороками
# print(func2(2,2))    #4

# def func3(x:int,y:int ) ->str:
#     return x*y
# print(func3(3,4))    #  позиционные аргументы
# print(func3(y = 8, x = 4))# именованные аргументы
# print(func3(x = 3,2)) # Error
# print(func3(3,x=2))# Error
# print(func3(3, y=3))

# *args, **kwargs

# def func4(x,y, *args):
#     #print(type(args))
#     #print(args)
#     return x +y + sum(args)
# print(func4(3,4,5,6,7,))    

# def func4(x,y, *args ,**kwargs):
#     print(kwargs)
#     return x +y + sum(args)
# print(func4(3,4,5,6,7, name = 'john',h = 'hello'))    


#  Мы используем *args  и **kwargs  в качестве аргументовб
#  когда заранее не известно сколько згачений мы хотим передать в функцию
# *args = для позиционных аргументов
# **kwargs - для имменовонных аргументов

# def func5(f = [], *args , **kwargs):
#     return sum(f) +sum(args) + sum(kwargs.values())
# # print(func5([1,2,3,4]))    
# # print(func5())
# list_ = [1,2,3,4]
# r = func5(list_,2, 3, 4, 2,a = 10, b = 10)
# print(r )
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

