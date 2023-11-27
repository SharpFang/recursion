def climb_stairs(n):
    if n <= 2:
        return n
    else:
        return climb_stairs(n - 1) + climb_stairs(n - 2)

# Приклад використання:
result = climb_stairs(3)
print(result)