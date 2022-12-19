"""
 Comprehension 28.11.22

 типы Comprehension :
  - List Comprehension - представление списков
  - set Comprehension - преставление множества
  -  dick Comprehension - преставление словаря
"""

# l = {'hello' for i in range(1,11)}
# print(l)
# l = ['john' for i in range(1,11)]
# print(l)
# n= int(input('Введите число:'))
# print('Четное') if n  % 2 == 0 else print('нечетное')

# l = [ i for i in range(0,10) if i % 2 == 0] # четное
# print(l)

# l = ['abc','hello','john', 'Sam']
# res = [ i for i in l if 'a' in i]
# print(res)

# res = [ i if i% 3 == 0 else i **2 for i in range(10)]
# print(res)
# res = [ 'Четное'  if i % 2 == 0 else 'нечетное' for  i in  range (10)  ]
# print(res)


# str_ = 'Hello my name is John and my surname is Snow'
# res = [ i  for i in str_ if i in 'aeiouy' ]
# print(res)
# get_ = 'Good moning 0707071831'
# res = [i for i in get_ if i in 'oig 7' ]
# print(res)

"""
Set coprehension - это почти тоже самое что и list comprehension, 
разница в том что выходные элементы не содержат дубликатов
"""

# s = { i for i in range(10)}
# print(s)
# res ={'Четное'  if i % 2 == 0 else 'нечетное' for  i in  range (10)  }
# print(res)

"""
Dict comprehension - аналогично создается, 
создаеться с дополнительным 
требованием определение ключа
"""

# {'key1' : 'values'}
# d = { i :i**2 for i in range(10)}
# print(d)

# l = [2, 5, 7, 6, 5]
# d ={i : 'Четное' if i %2 ==0  else 'нечетное' for i in l}
# print(d)

# res = {i :i **2 for i in range(10) if i % 2 == 0 }
# print(res)
# d = {'a': 5, 'b':6, 'c':3, 'd':1}
# res = {k :v for k, v, in d.items() if v % 2 == 0}
# print(res)
# res ={k:'Четное'  if v % 2 == 0 else 'Нeчетное' for k,v  in d.items()}
# print(res)


##########################
# matrix = [
#     [0,0,0],
#     [1,1,1],
#     [2,2,2]
# ]
# # l = []
# # for i in matrix:
# #    for j in i:
# #     l.append(j)
# # print(l)
# l = [ k for i in matrix for k in i  ]
# print(l)
