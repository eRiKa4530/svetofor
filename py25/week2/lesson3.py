# Словари +  методы Словарей 

# Словарей это изменяемый , упорядочный, итерируемый тип данных

#{} -  литералы

# dict_ = {}
# # print(type(dict_))
# print(dir(dict_))

# dict_ = {'name':'john','age':22, 'hobby':['fishing','football','auto']}
# #print(dict_['hobby'][1])
# #print(dict_['hobby'])
# print(dict_)

#Ключи долны быть уникальными и неизменяемымиб ф знфчения любыми

# d = {'age':20, 'age':50}
# d = {(1, 2): 'sasddsfa'}
# print(d)

# d = dict(name = 'john')
# print(d)


# d = {'age':22}
# d['age'] = 40
# d['name'] = 'john'
# print(d)

# Методы
# d = {'nmae':'john'}
# d.clear()
# print(d)

# l = ['name', 'age']
# dict_ = dict.fromkeys(l)
# dict_ = dict.fromkeys(l,'hello')
# print(dict_)

# d = {'age': 22, 'name': 'john'}
# # print(d['age2'])
# print(d.get('age2'))
# print(d.get('age2', 'не найдено!'))

# d ={'age':22,'name': 'john', 'last_name':'Snow'}
# d.pop( 'name')
# # print(d)
# # r = d.pop('name2','Нет такого ключа!')
# # print(r)
# # d.popitem() # Последнее значение
# print(d)

# d = {'name':'John','age':22}
#value = d.setdefault('name')
# value = d.setdefault('name3', 'nan') #возвращает значение ключа, если такого ключа нет, не вызывает ошибку 
# #а создает новый ключ с таким названием
# print(d)
# print(value) 

# d1 = {'age':23}
# d2 = {'name':'john'}
# d1.update(d2)
# print(d1)


#d ={'age':22,'name': 'john', 'last_name':'Snow'} 
# st_name':'Snow'}
# # print(d.keys())
# # print(d.values())
# # print(d.items())
# for i in d:
#     print(i)

# d ={'age':22,'name': 'john', 'last_name':'Snow'}
# for i in d:
#     print(i)

# for i in d.keys():
#        print(i)

# for i in d.values():
#          print(i)

# for i in d.items():
#     print(i)

# for k, v in d.items():
#     print('Это ключ - ', k)
#     print('Это значение - ', v)

# l = [1,2,3]
# l2=[1,2,3]
# print(l == l2) # по значением
# # print(l is l2) # по ячейка

# l = [1, 2,['hello', 'age']]
# l2 = l
# l2[0] = 'sfgfsfdg'
# print(l2)
# print(l

#Кортеж - неизменяемый , упорядочный,интерерируемый тип данных
# t = (1, 'hello', True, 1)
# # print(dir(t))
# print(t.count(1))
# print(t.index('hello'))
