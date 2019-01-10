# your code goes here
a,b=map(int,input().split(" "))
for num in range(a,b+1):
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				break
		else:
			if num == b:
				print(num,end="")
			else:
				print(num,end=" ")
