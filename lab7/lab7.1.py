# Создадим пустой словарь, в котором будут храниться данные студентов
students = {}

# Используем метод setdefault() для добавления данных студента в словарь
students.setdefault('John', {'age': 20, 'major': 'Computer Science'})
students.setdefault('Mary', {'age': 21, 'major': 'Business'})

# Используем метод update() для обновления данных студента в словаре
students.update({'John': {'age': 21}})
students.update({'Mary': {'major': 'Marketing'}})

# Используем метод get() для получения информации о студенте из словаря
john_age = students.get('John', {}).get('age')
mary_major = students.get('Mary', {}).get('major')
print(f'John: возраст - {john_age}')
print(f'Mary: специальность - {mary_major}')

# Используем метод pop() для удаления студента из словаря
removed_student = students.pop('Mary')
print(f'Удаленный студент: {removed_student}')

# Используем метод clear() для удаления всех студентов из словаря
clear_student_dict = students.clear()
print(clear_student_dict)