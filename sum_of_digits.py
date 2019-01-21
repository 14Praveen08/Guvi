number = int(input())
sum = 0
mod = 0
while number>0:
	mod = number % 10
	sum = sum + mod
	number = number // 10
print(sum)
