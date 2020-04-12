def rot_right(a):
	return zip(*a[::-1])
	
def sp(m, n ,start = 1):
	if n == 0:
		yield()
	else:
		yield tuple(range(start, m + start))
		for row in rot_right(list(sp(n - 1, m, m + start))):
			yield row
		
def spiral(m):
	return sp(m, m)
	
number = int(raw_input("Enter number for Spiral pattern:- "))

print "Spiral Matrix:- "
for row in spiral(number):
	print(join('%3i' % i for i in row))
