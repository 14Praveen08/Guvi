
q=int(input())
a=0
list1=list(map(int,input().split(" ")))
temp=list1.copy()
list1.sort()
list11=list1.copy()
for i in range(len(list11)):
	if(list11[i]==temp[i]):
		a=a+1
	else:
		break
print(a)
