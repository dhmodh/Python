year = 2000 		#Predecalare

if(year % 4) == 0:
	if(year % 100)== 0:
		if(year % 400) == 0:
			print(year,'is a leap yaer.')
		else:
			print(year,'is not leap year.')
	else:
		print(year,'is a leap yaer.')
else:
	print(year,'is a leap yaer.')
