#Класс Student
class Student:
    def __init__(self, name, cls):
        self.name = name
        self.cls = cls
    def __str__(self):
        return "ФИО: "+ self.name +" Класс: "+ self.cls

studentList = []
print("ФИО:")
name = input()
print("Класс")
cls = input()    
print()
while True:
    st = Student(name, cls)
    studentList.append(st)
    print("ФИО:")
    name = input()
    print("Класс")
    cls = input()
    print()
    if name == '' and cls == '':
        break

#Вывод списка
for student in studentList:
        print(student)
print()
studentList.sort(key=lambda x: x.cls)
#Вывод сортированного списка 
for student in studentList:
        print(student)