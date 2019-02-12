number = int(input())
list1=[]
for i in range(2,number+1):
	if number % i == 0 and i  % 2 == 0:
		list1.append(i)
print(' '.join(map(str,list1)))
