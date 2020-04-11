#Creating Set
my_set = {1, 2, 3 }
print(my_set)

#Add and Update Sets
my_set.add(4)
print(my_set)

my_set.update( [5, 6, 7] )
print(my_set)

#Removing Element from Set
my_set.discard(4)
print(my_set)

my_set.remove(6)
print(my_set)

#pop() and clear()
my_sets = {'a', 'b', 'c'}
returned_value = my_sets.pop()
print(my_sets)
print(returned_value)

my_sets.clear()
print(my_sets)
