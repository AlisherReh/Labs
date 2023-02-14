from random import randrange
min = 1
max = 49
nums = 6
ticket_nums = []
for i in range(nums):
    rand = randrange(min, max + 1)
    while rand in ticket_nums:
        rand = randrange(min, max + 1)
    ticket_nums.append(rand)
ticket_nums.sort()
print("Номера вашего билета: ", end = "")
for n in ticket_nums:
    print(n, end = " ")
print()