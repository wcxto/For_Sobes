# Напишите программу, которая принимает на вход целое число, и возвращает целое число, цифры в котором переставлены в обратном порядке. 

def reverse_integer(num):
    num_str = str(num)
    if num_str[0] == "-":
        reverse_str = "-" + num_str[:0:-1] 
    else:
        reverse_str = num_str[::-1]
