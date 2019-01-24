num1,num2=input().split(" ")
num2=int(num2)
li=[]
for i in range(len(num1)-1,len(num1)-num2-2,-1):
	li.append(num1[i])
li=li[::-1]
for i in range (len(li)):
	if(len(li)-1==i):
		print(li[i],end="")
	else:
		print(li[i],end="")
