# -*- coding: utf-8 -*-

# Есть функция генерации списка простых чисел

# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers


# # Часть 1
# # На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# # который выдает последовательность простых чисел до n
# #
# # Распечатать все простые числа до 10000 в столбик
#
# class GetPrimeumbers:
#
#     def __init__(self, n, number, prime_numbers):
#         self.n = n
#         self.number = number
#         self.prime_numbers = []
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.number += 1
#         if self.number > self.n:
#             raise StopIteration()
#         for prime in self.prime_numbers:
#             if self.number % prime == 0:
#                 break
#         else: self.prime_numbers.append(number)
#         return self.prime_numbers
#
# prime_number_iterator = GetPrimeumbers(n = 10000)
# for value in prime_number_iterator:
#     print(value)



# # Часть 2
# # Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# # Распечатать все простые числа до 10000 в столбик
#
#
# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#             yield prime_numbers[-1]
#
# for prime in get_prime_numbers(n=10000):
#     print(prime)




# Часть 3:
# Функции-фильтры:
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101

def prime_numbers_generator(n): #генератор простых чисел
    number, prime_numbers = 2, list()
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield prime_numbers[-1]


def lucky_number(number):
    number = [*map(int, str(number))] #приведение к списку
    n = len(number)
    return sum(number[:n//2]) == sum(number[(n+1)//2:])


# ## вызов функций
## первый способ
# # for prime_lucky_number in (number for number in prime_numbers_generator(n=10000) if lucky_number(number)):
# #     print(prime_lucky_number)

## второй способ (более читабельный)
# for prime_lucky_number in filter(lucky_number, prime_numbers_generator(n=10000)):
#     print(prime_lucky_number)
#
# def palindromic_number(number):
#     number = str(number)
#     return all(number[i] == number[-1 - i] for i in range(len(number) // 2))
#
# for prime_palindromic_number in (number for number in prime_numbers_generator(n=10000) if palindromic_number(number)):
#     print(prime_palindromic_number)







# Напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


# def every_minute_stat_generator(in_file):
#     group = None
#     count = 0
#     with open(file=in_file, mode='r') as input_file:
#         for line in input_file:
#             new_group = line[1: line.rfind(":")]
#             if group is not None and group != new_group:
#                 yield group, count
#                 count = 0
#
#             group = new_group
#             count += line.rfind('NOK', -4) != -1 #line.endswith('NOK') or line[: -1].endswith('NOK')
#
#         if group:
#             yield group, count
#
#
# grouped_events = every_minute_stat_generator(in_file='events.txt')
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')







# # Написать декоратор, который будет логировать (записывать в лог файл)
# # ошибки из декорируемой функции и выбрасывать их дальше.
# #
# # Имя файла лога - function_errors.log
# # Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# # Лог файл открывать каждый раз при ошибке в режиме 'a'
#
#
# def log_errors(func):
#     def surrogate(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except Exception as exc:
#             with open(file='function_errors.log', mode='a', encoding='utf8') as log_file:
#                 if args and kwargs:
#                     log_file.write(f'<{func.__name__}> <{args}> <{kwargs}> <{type(exc).__name__}> <{exc}>\n')
#                 elif args:
#                     log_file.write(f'<{func.__name__}> <{args}> <{type(exc).__name__}> <{exc}>\n')
#                 elif kwargs:
#                     log_file.write(f'<{func.__name__}> <{kwargs}> <{type(exc).__name__}> <{exc}>\n')
#                 raise
#     return surrogate
#
#
# @log_errors
# def check_line(line):
#     name, email, age = line.split(' ')
#     if not name.isalpha():
#         raise ValueError("it's not a name")
#     if '@' not in email or '.' not in email:
#         raise ValueError("it's not a email")
#     if not 10 <= int(age) <= 99:
#         raise ValueError('Age not in 10..99 range')
#
#
# lines = [
#     'Ярослав bxh@ya.ru 600',
#     'Земфира tslzp@mail.ru 52',
#     'Тролль nsocnzas.mail.ru 82',
#     'Джигурда wqxq@gmail.com 29',
#     'Земфира 86',
#     'Равшан wmsuuzsxi@mail.ru 35',
# ]
# for line in lines:
#     try:
#         check_line(line)
#     except Exception as exc:
#         print(f'Invalid format: {exc}')



