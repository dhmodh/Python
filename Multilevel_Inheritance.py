class University:
	def getUdetails(self):
		self.uName = input("Enter University Name:- ")
		self.uRID = input("Enter Reg. (University) number:- ")
		
	def showUdetails(self):
		print("University Name:- ",self.uName)
		print("University Reg. No.:- ",self.uRID)
		
class College(University):
	def getClgDetails(self):
		self.cName = input("Enter College name:- ")
		self.cRID = input("Enter College Reg. No.:- ")
		self.getUdetails()
		
	def showClgDetails(self):
		print("College Name:- ",self.cName)
		print("College Reg. No.:- ",self.cRID)
		self.getUdetails()
		
class Student(College):
	def getStudDetails(self):
		self.sName = input("Enter Student Name:- ")
		self.sRoll = input("Enter Student EnRoll No. :- ")
		self.sBranch = input("Enter Student's Branch:- ")
		self.getClgDetails()
		
	def showStudDetails(self):
		print("\nSTUDENT DETAIL",self.sName)
		print("Student Name:- ",self.s.Name)
		print("Student Enroll No. :- ",self.sRoll)
		print("Student Branch:- ",self.sBranch)
		self.showClgDetails()
		
s = Student()
s.getStudDetails()
s.showStudDetails()
