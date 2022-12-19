# Модули ,Пакеты .JSON

# Библиотека -  это просто набор модулей и пакетов


# Модули - Это файлы с разширением , который определяет некоторые классы, йункции или пременные. Эти модули
# могут быть импортирование при необходимости


# Пакеты - состоит из модулей , для того чтобы упакавоть файлы для удобства. 
# Первым файлом в пакете является ___init__.py


# math - модуль
# random - модуль
# functools -модуль
# time - модуль
# detetime -модуль

# from test_import import name,age
# from test_import import *
# print(name)
# print(age)

# from  my_package.test import last_name
# print(last_name)




# JSON  - (JavaScript OBject Notation) -  простой формат обмена даннымю Людям его легко читать и  вести
# в нем записи , компьютеры запросто справлются с его синтаксисом . В основном его применяется при передачи данных
#  между сервером и веб-приложением. ( для обмена данным между фронтом и беком)

# import json
# list_ = [True , 'hello', None, False]
# print(list_)
# json_obj = json.dumps(list_)
#  # Сериализация ( с python  B json)
# print(json_obj)
# python_obj = json.loads(json_obj)
# # Десериализация (c json B python )
# print(python_obj) 




# import json 
# d = {'a': True, 'b': False, 'c': None, 'd': 2}
# json_ = json.dumps(d)
# print(json_)
# python_obj = json.loads(json_)
# print(python_obj)


# import json
# with open('data.json') as file:
#     json_ = file.read()
#     print(json_)
#     pyth_ = json.loads
#     (json_)
#     python_obj = json.load(file)
#     print(pyth_)


# import json
# with open('data.json', 'w') as file:
#     list_ = [True, False, ' hello', None]
#     # json_obj = json.dumps(list_)
#     # print(json_obj)
#     # file.write(json_obj)
#     json.dump(list_,file)

# import json
# def get_names():
#     with open('data.json') as file:
#         python_ = json.load(file)
#     return python_
# def post_name(new_name):
#     python_ = get_names()
#     python_.append({'name': new_name})
#     with open('data.json','w') as file:
#         json.dump(python_,file)
# print(get_names())    
# post_name('Ranchek')
# print(get_names())

#CRUD
string = 'hello'
s = (str)
print(s)