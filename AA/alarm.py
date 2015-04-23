while True:
	times = map(int, raw_input().split())
	
	if sum(times)==0:
		break
	
	time_begin = times[0]*60 + times[1]
	time_end = times[2]*60 + times[3]
	
	if time_begin<=time_end:
		print time_end-time_begin
	else:
		print (1440-time_begin) + time_end
