# your code goes here
str1,str2 = map(str,input().split(" "))
list1=[]
list2=[]
count = 0
if len(str1) != len(str2):
	print("no")
else:
	for i in str1:
		list1.append(i)
	for i in str2:
		list2.append(i)
	for i in range(0,len(list1)):
		if list1[i] == list2[i]:
			break
		else:
			count=count+1
	if count>0:
		print("no")
	else:
		print("yes")
