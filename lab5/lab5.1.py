list = [['Alisher', '19', 'Satbayev'], ['Yernur', '20', 'AUES']]
for i in range(len(list)):
    print(list[i])
print()
list.append(['Darn', '20', 'MUIT'])
for i in range(len(list)):
    print(list[i])
print()
list.insert(0,['Beknur', '20', 'Satbayev'])
for i in range(len(list)):
    print(list[i])
print()
list.sort()
for i in range(len(list)):
    print(list[i])
print()
list.remove(['Beknur', '20', 'Satbayev'])
for i in range(len(list)):
    print(list[i])
print()
list.clear()
for i in range(len(list)):
    print(list[i])
print()

