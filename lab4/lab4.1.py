import math

#Функция для нахождения растояния
def rastoyanie(a, b):
    d = 0
    for i in range(2):
        d += math.pow(a[i] - b[i], 2)
    return d

#Класс Operation
class operation:
    def koordiante(self):
        koord = ['X', 'Y', 'Z', 'P']
        array = []
        for i in range(0, 4):
            b = []
            print('Координаты ', koord[i],': ')
            for j in range(2):
                n = int(input())
                b.append(n)
            array.append(b)

        max_dist = rastoyanie(array[0], array[1])
        for i in range(3):
            for j in range(i+1, 3):
                #Находим расстояние
                ras = rastoyanie(array[i], array[j])
                
                if ras > max_dist:
                    koord1 = i
                    koord2 = j
                    max_dist = ras

        print('Максимальное расстояние между ', koord[koord1] ,' и ', koord[koord2])

#Вызов метода
g = operation()
g.koordiante()