number = int(input())
frst = 0
temp = 0
second = 1
count = 1
print(second,end=" ")
while count < number:
	temp = frst + second
	frst = second
	second = temp
	count = count + 1
	if count == number:
		print(temp,end="")
	else:
		print(temp,end=" ")
	
