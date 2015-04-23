while True:
	pic = map(int, raw_input().split())
	
	if pic[0] == pic[1] and pic[0] == 0:
		break
	
	lines = pic[0]
	columns = pic[1]
	color = pic[2]
	
	if color == 1:
		ans = ((columns - 6)/2) * ((lines - 6)/2) + ((columns - 7)/2) * ((lines - 7)/2)
	else:
		ans = ((columns - 7)/2) * ((lines - 6)/2) + ((columns - 6)/2) * ((lines - 7)/2)
	
	print ans
