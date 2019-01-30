num1,num2 = map(int,input().split(" "))
num = list(map(int,input().split(" ")))
for i in range(0,num2):
	num = [num[-1]] + num[:-1]
print(' '.join(map(str,num)))
