# Имеются текст text и подстрока st. Напишите программу, которая находит индекс первого вхождения st в text.

# 1.1

def find_st(text, st):
    n = len(text)
    m = len(st)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i+j] == st[j]:
            j += 1
        if j == m:
            return i
    return -1


# Временная сложность этого алгоритма

import functools

def rabin_karp(text, st):
    if len(st) > len(text):
        return -1 
    BASE = 33
    text_hash = functools.reduce(lambda h, c: h * BASE + ord(c), text[:len(st)], 0)
    st_hash = functools.reduce(lambda h, c: h * BASE + ord(c), st, 0)
    power_st = BASE**max(len(st) - 1, 0) 
    for i in range(len(st), len(text)):
        if text_hash == st_hash and text[i - len(st):i] == st:
            return i - len(st) 
        text_hash -= ord(text[i - len(st)]) * power_st
        text_hash = text_hash * BASE + ord(text[i])
    if text_hash == st_hash and text[-len(st):] == st:
        return len(text) - len(st)
    return -1 

text = "В роще-чаще рыщет ящер, ищет пищи подходящей"
st = "ще"
print(rabin_karp(text, st))
