number = int(input())
frst = 0
temp = 0
second = 1
print(second,end=" ")
for i in range(0,number):
	temp = frst + second
	frst = second
	second = temp
	if i == number-1:
		print(temp,end="")
	else:
		print(temp,end=" ")
