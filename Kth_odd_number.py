num1,num2=map(int,input().split(" "))
list1=list(map(int,input().split(" ")))
c=0
for i in range(len(list1)):
	if(i%2!=0):
		c=c+1
		if(c==num2):
			break
	else:
		continue
print(list1[c])
