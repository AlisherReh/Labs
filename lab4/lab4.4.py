a = input()
b = input()
print()

while not(a.isdigit() and b.isdigit()):
    a = input()
    b = input()


sum = int(a) + int(b)
print(sum)