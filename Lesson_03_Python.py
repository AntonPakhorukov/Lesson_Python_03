# Функцию можно передавать целиком: ====================================================================================================

# def f(x):
#     return x**2
# print(f(5)) # 25
# print(type(f)) # function
# g = f
# print(g(3)) # 9
# print(type(g)) # function
# Объединение функций: =================================================================================================================

# def sum(x):
#     return x + x

# def mult(x):
#     return x * x

# def math(op, x): # op - передается функция. x - передается аргумент.
#     print(op(x)) # вывод функции от аргумента

# math(mult, 10) # 100 - 10 умножит на 10

# def sum(x, y):
#     return x + y
# def mult(x, y):
#     return x * y
# def calc(op, a, b):
#     print(op(a, b))
#     # return(op(a, b))
# calc(sum, 3, 5)
# f = mult
# calc(f, 5, 5)

# delit = lambda q, w: q / w
# # Варианты вывода:
# print(delit(16, 4))
# calc(delit, 20, 10)
# calc(lambda x, y: x - y, 30, 15)

# List Comprehension: =================================================================================================================
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# list1 = []
# for i in range(1, 51):
#     if (i % 2 == 0):
#         list1.append(i)
# print(f'list1  = {list1}')
# # В одну строку
# list2 = [i for i in range(1, 31) if i % 2 == 0]
# print(f'list2 = {list2}')
# # Кортежи:
# list3 = [(i, i) for i in range(1, 11) if i % 2 == 0]
# print(f'list3 = {list3}  - КОРТЕЖ') # [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10)]
# # с функцией:
# def f(x):
#     return x ** 3
# list4 = [f(i) for i in range(1, 5)]
# print(f'list4 = {list4}') # [1, 8, 27, 64]
# list4 = [(i, f(i)) for i in range(1, 5)]
# print(f'list4 = {list4}') # [(1, 1), (2, 8), (3, 27), (4, 64)]

# Задачка: ===========

# f = open('Text.txt', 'r') # связываем файловую переменную с файлом
# data = f.read() + ' ' # считываем все что есть в строчке и искусственно добавляем пробел
# f.close # закрываем файл
# print(data)
# print(len(data))
# numbers = [] # создаем пустой список
# while data != '': # пробегаемся по всей нашей строке и делаем проверку, пока моя строка не пустая
#     space_pos = data.index(' ') # находим первую позицию пробела
#     numbers.append(int(data[: space_pos])) # берем все что находится от перовго символа до позиции первого пробела, превращаем в число
#     # и добавляем в список номеров
#     data = data[space_pos + 1:] # обработка выборки - все что использовали, больше использовать не нужно
#     # print(data)
# print(data) # Будет пустой, так как пробежались выборкой
# print(numbers) # строку перевели в лист
# out = []
# for e in numbers:
#     if not e % 2: # Выбираем четные элементы 
#         out.append((e, e ** 2)) # записываем в лист, создавая кортеж
# print(out)

# ======================================================================================================================================

# def select(f, col):
#     return [f(x) for x in col]
# это по сути аналог функции 'map' - list(map(int, data))
# def where(f, col):
#     return [x for x in col if f(x)]
# это по сути аналог функции 'filter' - list(filter(lambda x: not x % 2, data))

# data = '1 2 3 5 8 15 23 38'.split() # - перевели строку в лист
# print(data) # ['1', '2', '3', '5', '8', '15', '23', '38'] 
# res = select(int, data) # строку изменили на числа
# print(res) # [1, 2, 3, 5, 8, 15, 23, 38]
# res = where(lambda x: not x % 2, res) # выбрали четные числа
# print(res) # [2, 8, 38]
# res = select(lambda x: (x, x**2), res) # сделали кортежи
# print(res) # [(2, 4), (8, 64), (38, 1444)]

# map: ===============================================================================================================================

# data = [x for x in range(1, 21)]
# print(data)
# data = list(map(lambda x: x + 10, data)) # при использовании map нужно делать явное преобразование
# print(data)

# li = list(map(int, input().split())) # Так можно создать лист чисел
# print(li)

# filter: =============================================================================================================================

# data = [x for x in range(1, 11)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)

# zip: ================================================================================================================================

# user = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 7, 14]
# data = list(zip(user, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 7), ('user5', 14)]
# # считает по нимаеньшему значению
# age = [32, 37]
# li = list(zip(user, ids, age))
# print(li) # [('user1', 4, 32), ('user2', 5, 37)]

# enumerate: ==========================================================================================================================

user = ['user1', 'user2', 'user3', 'user4', 'user5']
data = list(enumerate(user))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]