# Вычислите частное от деления x на y, где х и y – целые положительные числа. Допустимые операции – сложение, вычитание и побитовый сдвиг.

# Решение 1

def divide(x, y):
    quotient = 0
    remainder = x
    while remainder >= y:
        remainder -= y
        quotient += 1
    return quotient
