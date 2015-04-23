while True:
	try:
		n, l, c = map(int,raw_input().split())
	except EOFError:
		break
	
	string = raw_input().split()
	
	len_words = [len(s) for s in string]
	
	ans = 1
	counter = 0
		
	for i in range(n):
		if counter + len_words[i] <= c:
			counter += len_words[i] + 1
		else:
			counter = len_words[i] + 1
			ans += 1
	
	
	print (ans + l - 1) / l
				
