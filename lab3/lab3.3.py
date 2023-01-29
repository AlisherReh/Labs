import random

list = []

for i in range(0, random.randint(1, 10)):
    a = "{:.2f}".format((random.random()))
    list.append(a)

for i in enumerate(list):
    print(i)