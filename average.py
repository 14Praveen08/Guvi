number = int(input())
total = 0
series = list(map(int,input().split(" ")))
for i in series:
	total = total + i
ave = total // number
print(ave)
