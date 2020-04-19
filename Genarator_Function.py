def my_gen():
    n = 1
    print('This is Printed First.')
#Genarator Function contain Yield Statement
    yield n

    n += 1
    print('This is Printed Second.')
    yield n

for item in my_gen():
    print(item)