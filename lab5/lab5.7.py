def isSorted(lst):
    if lst == sorted(lst) or lst == sorted(lst, reverse=True):
        return True
    else :
        return False

list = []
n = int(input())
while n!=0:
    list.append(n)
    n = int(input())
print()
for i in range(len(list)):
    print(list[i], end=' ')
print()
print(isSorted(list))

