class Student:
	def getStudDetails(self):
		self.sName = input("Enter Student Name :- ")
		self.sRoll = input("Enter Student Roll Number :- ")
		
	def showStudDetails(self):
		print("\nSTUDENT DETAILS")
		print("Student Name :- ", self.sName)
		print("Student Roll Number :- ", self.sRoll)
		
class Academics(Student):
	total = 0
	def getMarks(self):
		for x in range(5):
			print("Enter Marks for Subject :- ", (x + 1), " :- ")
			self.marks = int(input())
			self.total = self.total + self.marks
			
	def getATotal(self):
		self.showStudDetails()
		return self.total
		
class Sports:
	spName = ""
	grade = 0
	
	def getSport(self):
		self.spName = input("Enter Sport Name :- ")
		self.grade = input("Enter Sport Marks :- ")
		
	def getSmarks(self):
		return self.grade
		
	def showSport(self):
		print("Sport Name :- ", self.spName)
		
class Result(Academics, Sports):
	def getResult(self):
		self.getStudDetails()
		self.getMarks()
		self.getSport()
		
	def showResult(self):
		aTotal = int(self.getATotal())
		sTotal = int(self.getSmarks())
		
		per = (aTotal + sTotal) / 6
		print("Percentage :- {:.2f}".format(per))
		self.showSport()
		
r = Result()
r.getResult()
r.showResult()
