number = int(input())
set = list(map(int,input().split(" ")))
set.sort()
length = len(set)
for i in range(length):
	if (i == len(set)-1):
		print(set[i],end="")
	else:
		print(set[i],end=" ")
