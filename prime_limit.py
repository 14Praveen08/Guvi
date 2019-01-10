# your code goes here
a,b = map(int,input().split(" "))
ans = []
for num in range(a,b+1):
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				break
		else:
			ans.append[num]
			
for i in range(len(ans)):
	if i == len(ans)-1:
		print(ans[i],end="")
	else:
		print(ans[i],end=" ")
