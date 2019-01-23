string = input()
list1 = []
for i in string:
	if((i>='a' and i<='z') or (i>='A' and i<='Z')):
		continue
	else:
		list1.append(i)
for i in range(0,len(list1)):
	print(list1[i],end="")
