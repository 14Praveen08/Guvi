number = int(input())
mod = 0
add = 0
while number > 0:
	mod = number % 10
	add = (mod * mod) + add
	number = number // 10
print(add)
