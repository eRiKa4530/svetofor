# Листы
'=========================List======================================' 

""""""
'List - это изменяемый , индексируемыйб итерируемыеб упорядоченны тип данных. Литералами листа являются []'
""""""

# list_ = []
# list_ = list()

# list_ = [1, 2, 'abc', 5, 3, 6, 3,[1,2,3], True,False None]

# list = [[1,2,3, [1,2,3]],[4,5,6],[7,8,9]]
# print(list[0][3][1], list_[1][0])

# list_ = [1,2,3, 'hello']
# print('hello' in list_)

"""
Напишите программу ,которая проверяет, есть ли введенное имя , в спискею Если есть ответить вы успушно вошли
, если нету , то сказать  у  вас нету доступа

names = [' sultan','vlad', 'ertay']
"""

# names = ['sultan','vlad', 'ertay']
# name = input(' Enter your names:')
# if name in names:
#      print('Вы успешно прошли')
# else:
#      print('Вы не прошли')


# names = input ('Enter names with spaces: '). lower().split()
# print(names)
# name = input ('Enter your name: ').lower()

# if name in names:
#     print('Success!')
# else:
#     print('Error!')

'===================Методы Listov============================'
# print(dir(list)
'append - добавление элемента в список'
#list_1 = [2, 5, 'hello']
# list_ =[]
# list_.append(125)
# print(list_)
 
'extend(другой лист)-  расширение одного листа засчет другого'
# list_1 = [10,20,30]
# print(list_1)
# list_2 = [1,2,3]
# print(list_2)
# list_1.extend(list_2)
# print(list_1)
# print(list_2)

'insert(куда и что) -  добавление  элемента по инедксу'
# list_ = [ 'n', 'e', 'l', 'l', 'o']
# list_.insert(3, 'ne')
# print(list_)
# list_ = [ 'n', 'e', 'l', 'l', 'o']
# list_.insert(3, [1,2,3]) #list_ = [ 'n', 'e', 'l', [1, 2, 3]'l', 'o']
# print(list_)'Ваш пароль должен хранить только числа'

'remove (x)- удаление элемента, если такого не существует выйдет исключение ValueError'
# list_ = [3, 1, 2, 3, 4, 5, 3]
# list_.remove(3)
# list_.remove(5)
# list_.remove(4)
# list_.remove(1)
# list_.remove(2)
# list_.remove(3)
# list_.remove(3)
# print(list_)

'pop(index) - удаляет элемент по идексу, если не указать индекс, то удалит последний элемент'
# list_ = [3, 1, 2, 3, 4, 5, 3, 6]
# removed_elem = list_.pop(1)
# print(removed_elem)
# print(list_)

'index(x, start and ) - возвращяет под каким индексом находиться "x"  можно задать начала и конец'
# list_ = [3, 5, 1, 3, 6, 4, 3 ]
# index_x = list_.index( 3)
# print(index_x)
# print(list_)

'cound(x) - считает кол-во "x" в списке'
# index_x = list_.index( 3)
# list_ = [5, 5, 5, 5, 5, 5]
# count_x = list_.count(5)
'reverse()- разворфчивает список'
# list_ = [1, 2, 3, 4,  5,ется

'reverse()- разворфчивает список'
# list_ = [1, 2, 3, 4,  5, 6,]
# list_.reverse()
# print(list_)

'copy() - поверхностное копирование списка'
# list_ = [0, 0, 0, 0, 0, [0, 0, 0, 1]]
# copy_list_ = list_.copy()
# # copy_list_[-1].append(1)
# print(copy_list_)
# print(list_)

'deepcopy - глубокое копирование, импортируестся через модуль copy'
# import copy
# list_ = [1, 2, 3, 4, 5,[0, 0, 0]]
# list_2 = copy.deepcopy(list_)
# list_2[-1].append(10)
# print(list_2)
# print(list_)

'clear() - очищает список'
# list_ = [1, 2, 3, 4]
# list_.clear()
# print(list_)
'==================range=============='
'range -  это генератор , в новой версии питора рн является типом данных'

# list_ = list(range(0, 100, 2) )
# print(list_) 
# print(range(5))

'==================Циклы(for, while)==================================='
"""
'Цикл for - это цикл, который выполняется до теч пор пока интерируемый обьек не закончиться
"""
# list_ = list(range(11)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_2 = []
# for i in list_: 
#       list_2.append(i)
# print(list_2)

""""""
'Цикл while - это циклб который выполняется до тех пор, пока условие True'

# i = 0 
# while i < 10 :
#      print('hello world')
# #
#      print(i)
#     i += 1

'break - "ломает", остановливает цикл в какой - то момент'
# i = 0 
# while i < 10 :
#    print('hello world')
#    if i == 5:
#      break
#    print(i)
#    i += 1 # i = i +1

'continue - пропускает итерацию'
# i = 1 
# while i < 10:
#    i += 1 
#    if i == 5:
#      continue
#    print('hello world')
   
# set = {1, 2, 3, 4, 5, 4}
# print(set)
