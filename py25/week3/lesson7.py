"""
Декаротары
"""


# def decorator_func(func):
#     print('Привет') 
#     return func()  

# def func1():
#     return'World'

# def func2():
#     return'heloo'   

# def func3():
#     return'john'     
# print(decorator_func(func1))
# print(decorator_func(func2))
# print(decorator_func(func3))


# def decor_func(func):
#     print('декоратор отработал')
#     return func()

# def func1():
#     print('Функция func1 отработла')
#     return'Hey'

# print(decor_func(func1))    

# def to_lower_case(func):
#      res = func().lower()
#      return res
# @to_lower_case
# def some_text():
#     return'Hello WORLD'

# print(some_text) # hello world

# def decor_func(func):
#     def wrapper(name):
#         print(f"Вы передали {name}")
#         return func(name)
#     return wrapper@call_function
# def first():
#     print("hello world")
#     return "hello world"
# first()

# # @decor_func
# # def get_name(name):
# #     return f'тебя зовут {name}'
# # print(get_name('john'))
# @call_function
# def first():
#     print("hello world")
#     return "hello world"
# first()

# def func_decor(func):
#     def wrapper():
#         print(' я код который сработал до вызова функции')
#         print(func())
#         print('Я код который сработал после')
#     return wrapper
# @func_decor
# def func1():
#     return'hello world'
# print(func1())
# def call_function(func):
#     def wrapper():
#         print('Вызываю фикцию' + "" + func.__name__)
#         print(func())
#         print(f'Вызoваю фукции ' + "" + func.__name__ + '' + 'прошёл успешно')
#     return wrapper
# @call_function
# def first():
#     # print("hello world")
#     return "hello world"
# first()


# def func_decor(func):
#     def wrapper(*args,**kwarg):
#         print(' я код который сработал до вызова функции')
#         print(func())
#         print('Я код который сработал после')
#     return wrapper
# @func_decor
# def func1():
#     return'hello world'
# print(func1())

# def decorator (func):
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         print(args)
#         print(kwargs)
#         func(*args,**kwargs)
#     return wrapper

# @decorator    
# def func_without_params():
#     print('Hello1')

# @decorator    
# def func_with_params(name):
#     print('Твое имя:', name)

# @decorator
# def func_with_params_kwargs(age):
#     print('Твое возраст', age)  

# func_without_params()
# func_with_params(3)
# func_with_params_kwargs(age=60)


# def div (func):
#     def wrapper (*args,**kwargs):
#        return '<div>'+ func(*args,**kwargs) + "</div"
#     return wrapper   

# @div
# def fanc1(name, last_name):
#     return name + ' ' + last_name

# def f1(func):
#     def wrapper (*args, **kwargs):
#         return  f'<f1> {func(*args,**kwargs)} </f1>'
#     return wrapper    
# @f1
# @div
# def func1(name,last_name):
#     return name +''+ last_name
# print(fanc1('John', 'Snow'))


# def decor_func(number):

#     def my_decorator(func):
#         def wrapper (*args, **kwargs):
#             print(number)
#             return func(*args, **kwargs)
#         return wrapper
#     return(my_decorator)
# def func1(age):
#     return age
# print(func1(3))
# def func_start_time(func):
#     from datetime import datetime
#     def wrapper():
#         date_time = datetime.datetime.now()
#         print(f'Функция запущена {date_time}')
#         return func()
#     return wrapper
    
# @func_start_time
# def func():
#     print('Hello world')
# func()





"""
Встроенное функция : 
"""



# all, any

# print(all([True,True])) #True
# print(all([True, False])) # False
# print(all([1,1,1,100])) # True
# print(all((0,1))) # False
# print(all(('hbjf', 5, [1], None))) #


# print(any([True, True])) # True
# print(any(([True, False]))) #True
# print(any('', None)) #False
# print(any((False, None,[],0,'',()))) #False


# l =[1, 2, 3, 4, 5, 6]
# res = [ i > 10 for i in l]
# print(any(res))
# print(any([i > 3 for i in l])) Это кароткий способ

# lambda -  это анонимная функция, которая имеет болле краткую 
# запись и чаще всего вызывается тоьько один раз
# def get_sum(x, y):
#     return x + y
# res = get_sum(4,3)    
# print(res)

# res = lambda x,y: x*y 
# print(res(4,5))
# r = lambda x: print(x)
# r('hellor ')


############ map

# j = [1, 2, 3, 4, 5]


# def get_str(x):
#     return str(x)
# # r2 = list(map(get_str,j))
# # print(r2)
# r3 = list(map(lambda x :str(x),j))
# print(r3)
# r =  list(map(str,j))
# print(r)

# j = [1, 2, 3, 4, 5]
# def func1 (x):
#     print(x)
#     return x + 2
# r1= list(map(func1,j))
# r2= list(map(lambda x: x +2,j))
# print(r1)
# print(r2) 
#######################################
# j = [80, 76, 34]
# # # def funk2(t):
# # #     print(t)
# # #     return (t+2)-15
# # # f1= list (map(funk2, j))
# # # print(f1)
# f1 = list(map(lambda f: f *2 ,j))
# print(f1)
# ###########################################

# вывести длинну строки
# l = ['hello', ' ajjn', ' jfh', 'vjd']
# r = list(map( len,l))
# print(r)
# d2 = list(map(lambda x: len(x),l))
# print(d2)

# def fkn(c):
#     return len(c)
# d3 = list(map(fkn,l))
# print(d3)

# l = [4, 3, 2, 1]
# r = list(map( lambda x: x>3,l))
# print(r)

# list_ = [5, 8, 4, 6, 7] 
# result = list(map(lambda x: x > 3, list_))
# print (result)
# list_ = [23, 45, 67, 87]
# r = list(map(lambda x : max(x) , list_))
# print(r)

### Filter
# l = [4, 3, 2, 1]
# r = list(filter(lambda x : x >3, l))
# # def fkg(j):
# #     return j >3
# # r2 = list(filter(fkg ,l))
# print(r)
# # print(r2)

# r = list(filter(lambda x: True, range (10)))
# # print(r)

############ reduce
# from functools import reduce
# # # print(sum(l))
# l = [1,2,3,4]
# r = reduce(lambda x, y : x +y,l)
# print(r)
#  r2 = reduce(lambda x,y : x if x < y else y,l)
# # print(r2)
# def gm(f,g):
#     return f + g 
# r3 = reduce(gm,l)
# print(r3)
# list_ = [23, 45, 67, 87]
# r = reduce(lambda x ,y: x if x> y else y , list_)
# print(r)

##################### zip
# k = ['John', 'sem', 'Non']
# d = [22,44,55,66]
# k2 = ['if','fj','dh']
# info = list(zip( k , d , k2))
# print(dict(zip(k, d)))
# print(info)

# j = ['john', 'Tom','Sam']
# res = enumerate(j ,)
# print(list(res))
# j = [' John','Sam']
# for i in enumerate(j):
#     print(i)
# string = 'hello'
# d = tuple(enumerate(string,))
# print(d)
# f = [1,2,3,4, 5]
# r = list(map(lambda x :' ч' if x % 2 == 0 else 'нч',f))
# print(r)

# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x : x >0,list_))
# print(result)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# from functools import reduce
# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = reduce(lambda x,y: x if len(x) > len(y) else y,list_ )
# print(result)

# from functools import reduce
# list_ = [5, 6, 7, 8] 
# result = reduce(lambda x,y : x+y,list_)
# print(result)

# list1 = ['THIS', 'IS', 'SOME','LIST'] 
# new_list1 = all(str.isupper() for str in list1) 
# print(new_list1) 

# list_ = [5, 8, 4, 6, 7]
# result = (i > 3 for i in list_)
# print( all([ i > 3 for i in list_]))

# list_ = [5, 8, 4, 6, 7]
# resualt = ( i < 0 for  i in list_)
# print(any([i < 0  for i in list_]))

# list_= [1, 2, 3, 4]
# result = list(filter(lambda x : for x %2 ==0,list_))
# print(result)

# list_= [1, 2, 3, 4]
# result = filter(lambda x : i if x %2 ==0,list_)
# print(result)
# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda x : x % 2 == 0,list_))
# print(result)
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list(filter(lambda x : len(x) > 7 , list_))
# print(result)

# list_ = [5, 6, 7, 8] 
# result = list(map(lambda x:))

# from functools import reduce
# list_ = [5, 6, 7, 8] 
# result = reduce(lambda x,y : x*y,list_)
# print(result)

# from functools import reduce
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# list2 = list(filter(lambda x : x%2 ==0, list_))
# list3 = list(filter(lambda x : x%2!= 0 ,list_))
# x = len(list2)
# y = len(list3)
# result = ( x,y )
# print(f'even:{result[0]}, odd: {result[1]}')
# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x :))

# for i in range (1,51):
#     if(i % 3 != 0 ):      
#      print(i)

# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# result = list(map(lambda x: abs(x) ,list_))
# print(result)

# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# print((1, 'k')>('b', 2))
# print((1, -1, 0)>(1, 1))

# divided = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]
# print(divided)
