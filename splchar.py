string=input()
splcount=0
for i in string:
	if i != " ":
		if i.isalnum():
			continue
		else:
			splcount = splcount +1
print(splcount)
