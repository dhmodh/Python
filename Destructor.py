class Vehicle:

        def __init__(self):

            print('Vehicle created.')

        def __del__(self):

            print('Destructor called, vehicle deleted.')

car = Vehicle()

print('Hello world')

#Destructor is defined using __del__() keyword:
