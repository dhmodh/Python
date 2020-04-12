num = int(raw_input("\nEnter n:- "));

for i in range(1, num + 1):
	for j in range(0 , i):
		print " ",((i + j) % 2),;
	print "\n";
