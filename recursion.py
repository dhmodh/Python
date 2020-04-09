def cal_sum(n):
	if n == 1:
		return 1
	else:
		return n + cal_sum(n-1)
		
sum = cal_sum(3)
print(sum)


#How this one Works........
#cal_sum(3) 			#1st call with 3
#3 + cal_sum(2)		#2nd call with 2
#3 + 2 + cal_sum(1)	#3rd call with 1
#3 + 2 + 1			#return from 3rd call as n=1
#3 + 3 				#return from 2nd call
#6					#return from 1st call
