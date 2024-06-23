# Вычислите частное от деления x на y, где х и y – целые положительные числа. Допустимые операции – сложение, вычитание и побитовый сдвиг.

# Решение 1

def divide(x, y):
    quotient = 0
    remainder = x
    while remainder >= y:
        remainder -= y
        quotient += 1
    return quotient


# Решение 2

def divide (x, y):
    result, power = 0, 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1
        result += 1 << power
        x -= y_power
    return result 
