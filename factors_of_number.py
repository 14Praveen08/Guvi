number = int(input())
list1= []
temp = number
while number != 0:
	if temp % number == 0:
		list1.append(number)
	number = number - 1
list1.sort()
for i in range(0,len(list1)):
	if i == (len(list1))-1:
		print(list1[i],end="")
	else:
		print(list1[i],end=" ")
