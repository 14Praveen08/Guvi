num1,num2 = map(int,input().split(" "))
diff = num1-num2
if diff == 0:
	print("even")
else:
	if diff % 2 == 0:
		print("even")
	else:
		print("odd")
