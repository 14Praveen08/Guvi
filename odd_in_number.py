number = int(input())
list1=[]
while number > 0:
	mod = number % 10
	if mod%2 != 0:
		list1.append(mod)
	number = number // 10
list1.sort()
for i in range(0,len(list1)):
	if i == (len(list1))-1:
		print(list1[i],end="")
	else:
		print(list1[i],end=" ")
		
