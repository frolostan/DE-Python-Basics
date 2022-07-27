# Основы Python. GU_Data_Engineering_1542 (31.01.2022)
# Выполнил: Фролов Виктор Сергеевич;
# Урок 5.


'''
1. Написать генератор нечётных чисел от 1 до n (включительно), используя
 ключевое слово yield.

'''

def odd_nums(n):
    for i in range(n):
        i = i * 2 + 1
        yield i


fib = odd_nums(15)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


# def odd_nums(max_value):
#     n = 1
#     while n <= max_value:
#         yield n
#         n += 2


# odd_to_15 = odd_nums(15)

# print(next(fib)) # StopIteration Checker to uncomment.

'''
 2.* (вместо 1) Решить задачу генерации нечётных чисел от 1 до n 
(включительно), не используя ключевое слово yield.

'''

max_val = 3
odd_nums_gen = (n for n in range(1, max_val + 1, 2))
print(next(odd_nums_gen))


# print(*((i * 2 + 1) for i in range(15)))

'''
3. Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида 
(<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка 
tutors. Если в списке klasses меньше элементов, чем в списке tutors, 
необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)

Доказать, что вы создали именно генератор. Проверить его работу вплоть
до истощения. Подумать, в каких ситуациях генератор даст эффект. 
 
'''


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(next(gen))

from itertools import zip_longest

gen = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses) if tutor is not None)
print(next(gen))

# from typing import Tuple

# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

# if len(klasses) > len(tutors):
#     while len(tutors) <= len(klasses):
#         tutors.append('None')


# def qqo1(list1, list2):
#     for i in range(len(list1)):
#         nama = tuple([list1[i], list2[i]])
#         yield nama


# n = qqo1(tutors, klasses)
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))

# # print(next(n))



'''
4. Представлен список чисел. Необходимо вывести те его элементы,
 значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

'''


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for i in range(len(src)):
    if src[i] > src[i - 1]:
        result.append(src[i])
print(result)

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(src)

# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_list = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
# print(new_list)


'''
5. Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать из этих элементов список с сохранением порядка их следования 
в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

'''


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([x for x in src if src.count(x) == 1])

