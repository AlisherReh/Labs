list = []

n = int(input())
while n!=0:
    list.append(n)
    n = int(input())
print()
list.reverse()
for i in range(len(list)):
    print(list[i])

