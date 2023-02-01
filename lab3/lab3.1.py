names = []
for i in range(5):
    name = input()
    names.append(name) 

k=0

while(names[k] != '' and k < 5):
    print(k+1, ' - элемент в листе: ', names[k])
    k+=1
