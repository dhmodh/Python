class Base:
	def cal_sum(self, a, b):
		return a + b
		
class Derived(Base):
	def cal_mul(self, a, b):
		return a * b
		
n1 = int(input("Enter 1st number:- "))
n2 = int(input("Enter 2nd number:- "))

d = Derived()

print("(From Base Class) Addition is:- ", d.cal_sum(n1, n2))
print("(From Derived Class) Multiplication is:- ", d.cal_mul(n1, n2))
