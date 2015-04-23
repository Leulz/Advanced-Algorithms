while True:
	try:
		n, r = map(int, raw_input().split())
	except EOFError:
		break
	volunteers = map(int, raw_input().split())
	total_vol = [False for x in (range(n+1))]
	ans = []
	
	if len(volunteers) == n:
		print '*'
		continue

	for i in volunteers:
		total_vol[i]=True

	for i in range(1, len(total_vol)):
		if not total_vol[i]:
			ans.append(i)
				
	print ' '.join(map(str, ans))+ ' '
