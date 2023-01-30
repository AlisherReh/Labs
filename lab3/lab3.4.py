#1
a = 5
b = 1
for i in range(a, b+1):
    print(i)

#2
if a<b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)

#3
for i in range(a - a % 2, b - b % 2, -2):
    print(i)

#4
sum1 = 0
sum2 = 0
n = 5
print("Номера карт:")
for i in range(1, n+1):
    sum1 += i
    
    print(i)

print()
print("После потери:")

for i in range(1, n):
    sum2 += int(input())

print()
print("Потерянная карта:")

print(sum1-sum2)
