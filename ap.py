# your code goes here
sum = 0
n,a,d = map(int,input().split(" "))
for i in range(0,n):
	sum = sum + a
	a = a + d
print(sum )
