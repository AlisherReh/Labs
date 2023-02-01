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
