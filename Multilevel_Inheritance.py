class Family:
	def show_family(self):
		print("This is my Family.")
		
#Father Class Inherited from family
class Father(Family):
	fathername = " "
	def show_father(self):
		print(self.fathername)
		
#Mother Class Inherited from family		
class Mother(Family):
	mothername = " "
	def show_mother(self):
		print(self.mothername)

#Son class Inherited from Father and Mother Classes 		
class Son(Father, Mother):
	def show_parent(self):
		print("Father :- ", self.fathername)
		print("Mother :- ", self.mothername)
		
s1 = Son()
s1.fathername = "Mark"
s1.mothername = "Sonia"
s1.show_family()
s1.show_parent()
