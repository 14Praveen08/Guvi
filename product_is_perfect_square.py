import math
num1,num2 = map(int,input().split(" "))
prod = num1 * num2
if (int(prod + 0.5) ** 2) == prod:
	print("yes")
else:
	print("no")
