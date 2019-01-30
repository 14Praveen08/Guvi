length = int(input())
string = input()
list1=[]
for i in string:
	if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
		continue
	else:
		list1.append(i)
list1.reverse()
print(''.join(map(str,list1)))
