# Работа с файлами

# file = open('task1.txt')
# print(file.read())
# print('*************')
# print(file.read())
# file.close()


# file = open('task1.txt','r')
# print(file.read(5))
# print('@@@@@@@@@@@@@@@')
# print(file.read())
# file.close()

# file = open('task1.txt','rt')
# print(file.tell())
# print(file.read())
# print(file.tell())
# print('**************')
# file.seek(5)
# print(file.read())
# file.close()


# file = open('text.txt','rt')
# some_text = file.read()
# print(some_text)
# print('**********')
# print(some_text)
# file.close


# file = open('task1.txt','rt')
# for i in file:
#     print(i)
# file.close


# file = open('task1.txt','rt')
# print(file.readline())
# file.close()

# file = open('task1.txt','rt')
# print(file.readlines())
# file.close()

# file = open('test2.txt','tr')
# file.read()
# file.close()



###
# r - открытие на чтение(является значением по умолчанию)
# w -  открытие на запись , содержимого файла удаляется, если файла не было создаст новый
# x - открытие на запись , сработывает в том случай если такого файла не существада( иначе ошибка)
# a - открытие на дозапись, информация добаляесть в концу
# b - открытие в двоичном режиме
# t - открытие в текстовом режиме (является  значением  по умолчением)
# + - открытие на чтение и запись


####
# file = open('text.txt','w')
# file.write('Hello World\n\n\n')
# file.write('john\t')
# file.close()


#####
# file = open('text3.txt','w')
# file.writelines(['vjdkj\n','snj\n'])
# file.close()


# try:
#     file = open('text3.txt','w')
#     file.write('hello\n')
# finally:
#     file.close()
#################### Легкий способ закрытие функций #################
# with open('text3.txt','w') as file:
#     file.write('Hello\n')
###########################################

# with open('text4.txt' , 'a') as f:
#     f.write('milk\n')

# with open('text4.txt', 'w')as f:
#     for i in range(0,10):
#         f.write(str(i) +'**2')
# # print()        
#     f.seek(0)
#     with open('text4.txt','r+') as f2:
#         print(f2.readlines)

# # with open('text5.txt','x') as file:
#     filr.write
    
# with open('text4.txt' , 'r+') as file:
#     print(file.read())
#     file.seek(0)
#     file.write('hello')
#     print(file.read())


# with open('text4.txt', 'w+')as file:
#     print(file.read())

# with open('image.jped','rd') as file:
#     # print(file.read())

#     with open('','wb')as file2:
#         file.write(file.read())


# 