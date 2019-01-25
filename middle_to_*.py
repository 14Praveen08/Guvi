string =  input()
s = len(string)
mid = 0
mid1 = 0
list1 = []
for i in string:
	list1.append(i)
if s % 2 !=0:
	mid = s // 2
	list1[mid] = "*"
	print(('').join(map(str,list1)))
else:
	mid = s//2
	mid1 = mid -1
	list1[mid] = "*"
	list1[mid1] = "*"
	print(('').join(map(str,list1)))
