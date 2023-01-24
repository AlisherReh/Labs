#вводим данные
name=str(input("Введите имя: ")) 
age =int(input("Введите свой возраст: "))
city=str(input("Введите где вы живете: "))

#вводим для ответа
answer = input('Введите для ответа "имя", "возраст", "место проживания": ')
if answer == "имя":
    print("Имя: ", name)
elif answer == "возраст":
    print("Имя: ", name)
elif answer == "место проживания":
    print("Имя: ", name)
else: print("такого вариянта не существует")
