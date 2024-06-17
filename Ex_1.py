# Напишите программу, которая принимает на вход целое число, и возвращает целое число, цифры в котором переставлены в обратном порядке. 

# v1
def reverse_integer(num):
    num_str = str(num)
    if num_str[0] == "-":
        reverse_str = "-" + num_str[:0:-1] 
    else:
        reverse_str = num_str[::-1]


# v2
def reverse_integer(num):
    result, num_remaining = 0, abs(num)
    while num_remaining:
        result = result * 10 + num_remaining % 10
        num_remaining //= 10
    return -result if num < 0 else result


# Сравним быстродействие решений:

import timeit

def reverse_integer_1(num):
    result, num_remaining = 0, abs(num)
    while num_remaining:
        result = result * 10 + num_remaining % 10
        num_remaining //= 10
    return -result if num < 0 else result

def reverse_integer_2(num):
    num_str = str(num)
    if num_str[0] == "-":
        reverse_str = "-" + num_str[:0:-1] 
    else:
        reverse_str = num_str[::-1]
    return int(reverse_str)

# Тестируем на случайном числе из 10000 цифр
num = int("".join(str(i % 10) for i in range(10000)))

# Сравниваем время выполнения двух функций
t1 = timeit.timeit(lambda: reverse_integer_1(num), number=100)
t2 = timeit.timeit(lambda: reverse_integer_2(num), number=100)
print(f"Время выполнения решения с циклом: {t1:.6f} секунд")
print(f"Время выполнения с методом строк: {t2:.6f} секунд")
