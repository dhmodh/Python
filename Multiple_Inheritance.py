class CementDealer:
	def getCementDealer(self, quantity):
		return quantity * 300
		
class IronDealer:
	def getIronCost(self, quantity):
		return quantity * 4500
		
class Builder(CementDealer, IronDealer):
	def getTotalCost(self, cQ, iQ):
		c_cost = self.getCementDealer(cQ)
		i_cost = self.getIronCost(iQ)
		totalCost = c_cost + i_cost
		return totalCost
		
cement = int(input("Enter the Cement Quantity:- "))
iron = int(input("Enter the Iron Quantity:- "))

b = Builder()

total_cost = b.getTotalCost(cement,iron)

print("TOTAL COST:- ",total_cost)
