from functools import reduce

my_list = [1, 2, 3, 4, 5]

# пример использования функции map применяет функцию ко всем элементам
squared_list = list(map(lambda x: x ** 2, my_list))
print(squared_list)

# пример использования функции filter фильтрует элементы
even_list = list(filter(lambda x: x % 2 == 0, my_list))
print(even_list)

# пример использования функции reduce применяет функцию к каждому элементу и выводит одно значение
product = reduce(lambda x, y: x * y, my_list)
print(product)
