def my_pow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / my_pow(x, -n)
    elif n % 2 == 0:
        half_pow = my_pow(x, n // 2)
        return half_pow * half_pow
    else:
        return x * my_pow(x, n - 1)

# Приклад використання:
result = my_pow(2.00000, 10)
print(result)