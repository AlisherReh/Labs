
my_tuple = (1, 2, 3, 4, 5)
my_set = {3, 4, 5, 6, 7}

# function 1: len()
print("Tuple length:", len(my_tuple))   
print("Set length:", len(my_set))       

# function 2: union()
my_new_set = my_set.union({8, 9, 10})
print("Union of sets:", my_new_set)    

# function 3: index() 
print("Index of 3 in tuple:", my_tuple.index(3))

# function 4: add()
my_set.add(8)
print("Set after adding 8:", my_set)

# function 5: count()
print("Count of 4 in tuple:", my_tuple.count(4))  

