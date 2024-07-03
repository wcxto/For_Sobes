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
