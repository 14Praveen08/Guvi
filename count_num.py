# your code goes here
number=int(input())
temp = 0
while number != 0:
	number = number // 10
	temp = temp + 1
print(temp)
