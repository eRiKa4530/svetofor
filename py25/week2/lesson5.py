# Множества(set) в Python
# Множества это изменяемый, неупорядоченный

# set, или множество, это изменяемая, неупорядоченная коллекция уникальных значений.



#{} - литералы
# s = set()
# s = {1, 2, 'hello' , 4, }
# s = {1,1,1,1,1,1}
# print(s)

# s = {True, 4, None, (1, 2, 3 )}
# print(s)

# l = [1, 2, 3, 2, 2, 2, 2]
# print(set(l)) #удалить дублиру. значение

# s = {1, 2, 2, 2, 2}
# print(len(s)) #2

# s = {'Hello', 'John', 1, 2, 3 }
# print('John' in s)

# FizzBuzz
# Вместо чисел кратных трем, программа должна печатать Fizz. Вместо чисел кратных пяти - 'Buzz'.
# Если число кратно  и трем , и пяти , программа долна печатать 'FizzBuzz'

# l = range(101)
# for i in l:
#     if i % 3 == 0 and i % 5 == 0:
#          print('FizzBuzz')
#     elif i % 5 == 0:
#         print('Fizz')
#     elif i % 5 == 6:   
#         print('Buzz')


# l = [1, 2, 3, 4, 5]
# i = 0
# while i < len(l): # 0 < 6
#     print(l[i]) # 
#     i += 1

# l = [1, 3, 4, 5, 6]
# # # Это число 1 и его индекс 0
# x = 0
# for i in l :
#     print(f 'Это число {i}  и его индекс иего индекс {x}')
#     x += 1

# for i in range(len(l)):
#     print(f 'Это число {l[i]}  и его индекс {i} ')



# l = [1, 3, 4, 5, 9]
# for i in l:
#     if i == 4:
#     continue    
# print(i)

# import random 
# # print(random. randint(-100,100))

# l = ['Red','Green']

# i = 0 
# count_green  = 0
# count_red = 0
# while i < 20:
#     team_ = random.choice(l)
#     print(team_)
#     i += 1
# if  team_== 'Red' :
#     count_red += 1
# else :
#     count_green += 1
#     i += 1
# # print(count_green)
# # print(count_red)
# if count_green > count_red:
#     print(' Win Green')
# elif count_red > count_green:
#     print('Win Red')   
# else: 
#     print('Win дружба') 


# num = 712
# a = 7
# f = 1 
# d = 2
# print(a+f+d )
# num = 712
# res = 0
# for i in str (num):
#     res += int(i)
# print(res)

# mun = 87378
# tes = 0 
# for i in str(mun):
#     tes += int(i)
# print(tes)




# a = {'Jane', 'Eyre', 22} 
# a.set.update('heloo')
# print(a)
# a = {  'Jane', 'Eyre',22   }  
# a.add('Hello world')
# print(a)
# a = {1, 2, 3 }
# b = {3, 4 }
# b.update(a)
# print(b)
# a = {1, 2, 3, 4, 5}
# a.discard(6)
# print(a)
# a = {1, 2, 3, 4, 5}
# a.remove(8)
# print(a)
# set = {1, 2, 3, 4}
# set.clear() 
# print(set)
# a = {4, 6, 100, -45, -6}
# b = {4, 5, -5, -6}
# s = a.intersection(b)
# print(s)

# a = {2, 4, 6, 50, -45, -6}
# b = {4, 3, 5, -5, -6}
# s = b.intersection(a)
# print(s)
# 
# a = {2, 4, 5, -45, -6}
# b = {4, 3, 5, -5, 2}
# s = a.union(b)
# print(s)
# a = ['Jane','Eyre',22  ]
# a.append('Hello world')
# print(a)
