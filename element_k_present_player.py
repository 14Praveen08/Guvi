count  = 0
num1,num2 = map(int,input().split(" "))
li = list(map(int,input().split(" ")))
li.sort()
for i in li:
	if  num2 == i:
		count =  count + 1
if count > 0:
	print("Yes")
else:
	print("No")
