# #1 Умножение всех чисел в списке
# from math import prod

# nums = [2, 3, 4, 5]
# result = prod(nums)
# print(result)

# #2 Подсчёт заглавных и строчных букв в строке
# s = "Hello World"

# u = sum(c.isupper() for c in s)
# l = sum(c.islower() for c in s)

# print("Uppercase:", u, "Lowercase:", l)

# #3 Проверка, является ли строка палиндромом
# import math

# def is_palindrome(s):
#     return s == s[::-1]

# s = "madam"
# print(is_palindrome(s))

#4 Вычисление квадратного корня через заданное количество миллисекунд
import math
import time

def delayed_sqrt(n, ms):
    time.sleep(ms / 1000)
    print(f"Square root of {n} after {ms} milliseconds is {math.sqrt(n)}")

n = 25100
ms = 2123
delayed_sqrt(n, ms)

# #5 Проверка, являются ли все элементы кортежа True

# def all_true(t):
#     return all(t)

# t = (True, True, False)
# print(all_true(t))