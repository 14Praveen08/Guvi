temp = 0
number = int(input())
for i in range(1,11):
	if i == number:
		temp=temp+1
if temp == 1:
	print("yes")
else:
	print("no")
