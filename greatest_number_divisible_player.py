maxi = 1
num1,num2 = map(int,input().split(" "))
if num1 > num2:
	i=num1
else:
	i=num2
for j in range(1,i):
	if num1 % j == 0 and num2 % j == 0:
		if j>maxi:
			maxi=j
print(maxi)
