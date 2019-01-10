a,b = map(int,input().split(" "))
ans=[]
for i in range(a+1,b):
	if i==b-1:
		if i%2==0:
			ans.append(i)
	else:
		if i%2==0:
			ans.append(i)
for i in range(len(ans)):
	if i==len(ans)-1:
		print(ans[i],end="")
	else:
		print(ans[i],end=" ")
