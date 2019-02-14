num1,num2 = map(int,input().split(" "))
count = 0
while num1 !=1:
	if num1 % num2 == 0:
		print("no")
		count = 1
		break
	
	num1 = num1 // num2
if count==0:
	print("yes")
	
