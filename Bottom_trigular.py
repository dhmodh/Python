n = int (input("Enter Number of Rows:- "))

for i in range (n, 0, -1):
	print((n-i) * ' ' + i * '*' )
