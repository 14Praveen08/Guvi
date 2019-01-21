string = input()
a=0
f=0
for i in string:
	if(i.isnumeric()):
		a = a + 1
	elif(i.isalpha()):
		f = f + 1
	else:
		continue
if(a>0 and f>0):
	print("Yes")
else:
	print("No")
