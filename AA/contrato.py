while True:
	d, n = map(int, raw_input().split())
	
	if d == 0 and n == 0:
		break
	
	num_list = map(int, str(n))
	
	for i in range(len(num_list)-1, -1, -1):
		if num_list[i]==d:
			num_list.pop(i)
	
	if len(num_list)==0:
		print 0
	else:
		resp = int(''.join(map(str, num_list)))
		print resp
