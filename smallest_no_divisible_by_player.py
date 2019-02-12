num,num1 = map(int,input().split(" "))
if num > num1:
	greater = num
else:
	greater = num1
while(True):
	if((greater % num == 0) and (greater % num1 == 0)):
		lcm = greater
		break
	greater = greater + 1
print(lcm)
