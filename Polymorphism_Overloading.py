class Parent: 	#define a Parent class
	def myMethod(self):
		print("Calling Parent Method")
		
class Child(Parent):
	def myMethod(self):
		print("Calling Child Method")
		
c = Child() 	#instance of child
c.myMethod() 	#child calls overridden				
