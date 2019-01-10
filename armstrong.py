# your code goes here
number=int(input())
t=str(number)
p=len(t)
c=0
temp=number
while number>0:
	y=number%10
	b=y**p
	c=c+b
	number=number//10
if temp==c:
	print("yes")
else:
	print("no")
