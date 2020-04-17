def hanoi(x):
	if x == 1:
		return 1
	else:
		return 2 * hanoi(x-1) + 1
		
x = int(input("Enter the Number of Disks :- "))

print('Number of Steps :- ', hanoi(x))
