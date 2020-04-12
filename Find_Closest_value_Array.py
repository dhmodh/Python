closest = 0

array = list()
num = raw_input("Enter the number of element:- ")

print
print 'Enter' + str(num) + 'number in Array'
for i in range(int(num)):
	n = raw_input("num" + str(i+1)+": ")
	array.append(int(n))
	
print
print "Numbers are:- "
print array

print
find = int(raw_input("Enter Number to find Closest value:- "))

distance = abs(closest - find)
for i in range(1, len(array)):
	distancel = abs(array[i] - find)
	if distance > distancel:
		closest = array[i]
		distance = distancel

print
print "Closest Value is:- ",closest 
