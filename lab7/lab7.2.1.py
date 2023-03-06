'''
3
Россия: Волга, Обь, Лена
Канада: Маккензи, Йукон, Сен-Лоуренс
Бразилия: Амазонка, Парана, Уругвай
Волга, Парана, Лена
Маккензи
Италия: По

'''

# Ввод числа элементов в словаре
n = int(input())

# Создание пустого словаря для хранения данных
countries = {}

# Ввод данных о странах и реках
for i in range(n):
    # Считываем строку вида "Страна: река1, река2, ..."
    country_data = input().split(": ")
    # Разделяем названия рек и сохраняем их в списке
    rivers = country_data[1].split(", ")
    # Записываем название страны и список рек в словарь
    countries[country_data[0]] = rivers

# Ввод списка названий рек
river_names = input().split(", ")

# Задание 1: вывод стран, в которых протекает каждая река
for river_name in river_names:
    for country_name, rivers in countries.items():
        if river_name in rivers:
            print(f"{river_name} протекает в {country_name}")

# Задание 2: проверка наличия реки в словаре
check_river_name = input()
if any(check_river_name in rivers for rivers in countries.values()):
    print(f"Река {check_river_name} присутствует в словаре")
else:
    print(f"Река {check_river_name} отсутствует в словаре")

# Задание 3: добавление новой пары страна-река в словарь
new_country_name, new_river_name = input().split(": ")
if new_country_name in countries:
    countries[new_country_name].append(new_river_name)
else:
    countries[new_country_name] = [new_river_name]

# Вывод обновленного словаря
print(countries)
