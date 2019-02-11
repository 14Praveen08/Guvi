list1=[]
string = input()
for i in string:
	if i.isupper():
		list1.append(i.lower())
	else:
		list1.append(i.upper())
print(''.join(map(str,list1)))
