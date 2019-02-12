# your code goes here
count = 0
number  = int(input())
while number!=1:
	if number %  2 !=0:
		print("no")
		count = 1
		break
	number =  number  // 2
if count==0:
	print("yes")
