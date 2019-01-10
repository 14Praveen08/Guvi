# your code goes here
a,b = map(int,input().split(" "))
for i in range(a+1,b):
	if i==b-1:
		if i%2!=0:
			print(i,end="")
	else:
		if i%2!=0:
			print(i,end=" ")
