num1,num2 = map(int,input().split(" "))
sum = num1+num2
if sum == 0:
	print("even")
else:
	if sum % 2 == 0:
		print("even")
	else:
		print("odd")
