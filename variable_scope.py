def my_func():
	x = 10					#This x is local in my_func()
	print("value inside Function:- ", x)
	
x = 20						#This x is defined in Global scope
my_func()
print("Value Outside Function:- ", x)
