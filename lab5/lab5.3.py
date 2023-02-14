subjects = [0, 'math','history','english']
Alisher_grades = ['Alisher',5, 4, 5]
Yernur_grades = ['Yernur',2, 2, 2]
Darn_grades = ['Darn',4, 4, 5]
n = input()
for i in range(1, len(subjects)):
    if(Alisher_grades[0] == n):
        print(subjects[i], '-' ,Alisher_grades[i])
    if(Yernur_grades[0] == n):
        print(subjects[i], '-' ,Yernur_grades[i])
    if(Darn_grades[0] == n):
        print(subjects[i], '-' ,Darn_grades[i])

