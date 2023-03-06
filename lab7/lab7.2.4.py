'''
5
Иванов 14 мая
Петров 1 июня
Сидоров 25 мая
Козлов 3 июля
Федоров 14 мая
май

'''

n = int(input()) # количество сотрудников
vacations = {} # словарь для хранения графика отпусков

# заполнение словаря
for i in range(n):
    name, day, month = input().split()
    if month not in vacations:
        vacations[month] = [name]
    else:
        vacations[month].append(name)

# обработка запроса
query_month = input()
if query_month in vacations:
    print(" ".join(vacations[query_month]))
else:
    print()
