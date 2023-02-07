print('Введите текст')
s = input()

print()
print('Все слова с большой буквы')
print(s.title())
print()

print('Вверхний регистр')
print(s.upper())
print()
print('Слово в кавычках')
s = input()
print(s[s.find('(') + 1:s.find(')')])
print()
print('Нижний регистр:')
print(s.lower())
print()

str = "чтобы сделаться не абстрагировать" 
print(str)
print('Слово в конце которой буква "я" ')
for i in str.split(): 
    if(i.endswith("я")): 
        print(i) 
print()

s = input('Введите текст две первые буквы "a" заменятся: ')
n = len(s)
s = s[:n // 2].replace('a', '*') + s[n // 2:]
print(s)
print()
print('Введите букву количество которой хотите найти')
print('Количество - ',s.count(input()))
print()
price = int(input('Введите цену за еду: '))
s = "Покупайте еду за {price:.2f} тенге"
print(s.format(price))