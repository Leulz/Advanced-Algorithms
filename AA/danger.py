while True:
	entrada = raw_input()
	if entrada == '00e0':
		break
	
	num = int(entrada[0])*10 + int(entrada[1])
	num = num* (10**int(entrada[3]))
	
	if num==1 or num==2:
		print 1
		continue
	else:
		pot = 2
		while pot*2<=num:
			pot*=2
		print 1 + ((num-pot)*2)
