number = int(input())
hour = 0
min = 0
if number < 60:
	print(hour,end=" ")
	print(number)
else:
	hour = number // 60
	min = number % 60
	print(hour,end=" ")
	print(min)
