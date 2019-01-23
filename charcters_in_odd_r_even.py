# your code goes here
string = input()
list1 = []
list2 = []
for i in range(0,len(string)):
	if i % 2 == 0:
		list1.append(string[i])
	else:
		list2.append(string[i])
print(''.join(map(str,list1)),end=" ")
print(''.join(map(str,list2)))
