# your code goes here
number  = int(input())
count = 0
for i  in range(0,number+1):
	if i % 1 == 0 and i % 2  == 0:
		count =  count + 1
print(count)
