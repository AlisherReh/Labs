import random
import matplotlib.pyplot as plt

# Сгенерируем данные для графика
x = list(range(1, 11))
y = [random.randint(1, 10) for i in range(10)]

# Нарисуем линейный график
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Линейный график')
print('max of y = ',max(y), ', min of y = ', min(y), ', линейный график')
print()
# Сгенерируем данные для гистограммы
data = [random.randint(1, 10) for i in range(100)]

# Нарисуем гистограмму
plt.figure()
plt.hist(data)
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Гистограмма')
print('max of data = ',max(data), ', min of data = ', min(data), ', гистограмма')
print()
# Сгенерируем данные для диаграммы рассеяния
x = [random.randint(1, 10) for i in range(50)]
y = [random.randint(1, 10) for i in range(50)]

# Нарисуем диаграмму рассеяния
plt.figure()
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Диаграмма рассеяния')
print('max of x = ',max(x), ', min of x = ', min(x), ', диаграмма рассеяния')
print('max of y = ',max(y), ', min of y = ', min(y), ', диаграмма рассеяния')

# Выведем графики на экран
plt.show()
