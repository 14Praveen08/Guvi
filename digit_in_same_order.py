number=int(input())
list = []
while number>0:
	mod = number % 10
	list.append(mod)
	number = number // 10
lii=list[::-1]
for i in range(0,len(lii)):
	if(i==len(lii)-1):
		print(lii[i],end="")
	else:
		print(lii[i],end=" ")
