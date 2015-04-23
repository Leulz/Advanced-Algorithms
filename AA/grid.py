while True:
	try:
		n = int(raw_input())
	except EOFError:
		break
	
	before = map(int, raw_input().split())
	after = map(int, raw_input().split())
	
	index_before = [0 for x in range(n+1)]
	index_after = [0 for x in range(n+1)]
	
	for i in range(n):
		index_before[before[i]] = i
	
	for i in range(n):
		index_after[after[i]] = i
	
	ans = 0
	
	for i in range(n+1):
		for j in range(n+1):
			if index_before[j]<index_before[i] and index_after[j]>index_after[i]:
				ans += 1
	
	print ans
