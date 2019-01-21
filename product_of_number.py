number = int(input())
prod = 1
while number > 0:
	mod = number % 10
	prod = prod * mod
	number = number // 10
print(prod)
