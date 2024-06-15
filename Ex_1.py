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
