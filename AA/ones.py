while True:
	try:
		n = int(raw_input())
	except EOFError:
		break
	
	ans = 1
	r = 1
	
	while (r!=0):
		r = ((r%n * 10%n) % n + 1%n) % n
		ans += 1
	print ans
		
