count = 0
count1  = 0
string = input()
for  i in string:
	if i == "(":
		count = count + 1
	else:
		count1 = count1 + 1
if  count == count1:
	print("yes")
else:
	print("no")
