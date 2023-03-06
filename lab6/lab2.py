import random

def fill_tuple(n, low, high):
    return tuple(random.randint(low, high) for _ in range(n))

# Заполнение
t1 = fill_tuple(10, 0, 5)
t2 = fill_tuple(6, -5, 0)

# Третий
t3 = t1 + t2

# Количество
num_zeros = t3.count(0)

# Вывод
print("Third tuple:", t3)
print("Number of zeros:", num_zeros)
