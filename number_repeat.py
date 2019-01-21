n,k = map(int,input().split(" "))
li = list(map(int,input().split(" ")))
count = 0
for i in range(0,len(li)):
	if(li[i]==k):
		count = count + 1
print(count)
