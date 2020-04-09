n_term = 10
# First Two terms
n1 = 0
n2 = 1
count = 0

print("Fibonacci Sequence upto",n_term,":-")

while count < n_term:
	print(n1)
	nth = n1 + n2
	
	#Update values
	n1 = n2
	n2 = nth
	count+=1

