# список чисел
numbers = []
while True:
    n = int(input())
    numbers.append(n)
    if n==0:
        break

# проверяем есть ли в списке хотя бы одно четное число
if any(num % 2 == 0 for num in numbers):
    print("В списке есть четное число")
else:
    print("В списке нет четных чисел")

# проверяем все ли элементы списка кратны 2
if all(num % 2 == 0 for num in numbers):
    print("Все элементы списка кратны 2")
else:
    print("Не все элементы списка кратны 2")
