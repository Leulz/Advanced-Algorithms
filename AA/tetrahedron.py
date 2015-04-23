n = int(raw_input())

mod = 1000000007

def calc(y):
	x = 1
	prev = 0
	threes = 1
	if y == 1:
		return 0
	elif y == 2:
		return 3
	
	for fraction in range(n-1):
		x = threes * 3
		threes *= 3
		threes = threes % mod
		x = x % mod
		x = x - prev
		prev = x
	
	return x % mod

print calc(n)
