# def get_string_length(str):
#     counter = 0 
#     for i in str:
#         counter += 1
#     return counter
# str = 'hello'        
# print(get_string_length('hello')) 
# def get_type( a,b):
#     a = type(a)
#     b = type(b)
#     print(a)
#     print(b)
# print(get_type(5, 's') )

# def func1(x,y):
#     try:
#         return x/y
#     except ZeroDivisionError :   
#            return 'На ноль делить  нельзя'
# print(func1(5,0))
#     
# def func2(num1, num2):
#     res = list(range(num1 , num2))
#     return res
# print(func2(1,6))
# def func3(a=5, b = 10):
#     print(a,b)
# func3(1,2)    
# func3(a=1, b =2)
# func3(b = 1 ,a=2)
# func3(1,b =2)
# func3()
# func3(1)

# def is_eval(num: int) -> bool:
#     if num %2 == 0:
#         return True
#     return False

# print(is_eval(4)) # True
# print(is_eval(5)) # False
# from time import sleep
# def func5(num):
#     for i in range(num):
#        sleep(1)
#        print(i)
# func5(5)

# def is_palindrom(str_):
#     if str_ == str_[::-1]:
#         return True
#     return False
# print(is_palindrom('ovo'))    
# print(is_palindrom('hello'))

# from datetime import date
# #print(date.today().weekday())
# taday_weekday = date.today().weekday()
# list_weekday = ['Пн', 'Вт','Ср','Чт','Пт','Сб','Вс']

# def week(index_day, list_days):
#     return f'Привет сегодня {list_days[index_day]}'
# print(week(taday_weekday, list_weekday))       

def is_palindrom(str_):
    if str_ == str_[::-1]:
        return True
    return False
print(is_palindrom('ovo'))    
print(is_palindrom('hello'))
