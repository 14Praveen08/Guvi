number=int(input())
ind=0
arr = list(map(int,input().split(" ")))
for i in arr:
	ind = arr.index(i)
	print(i,end=" ")
	print(ind)
