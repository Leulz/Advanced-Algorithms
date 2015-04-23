nt = [int(x) for x in raw_input().split()]

n = nt[0]
t = nt[1]

sequence = [int(x) for x in raw_input().split()]

current_pos = 0

for i in range(n-1):	
	current_pos = (current_pos)+sequence[current_pos]
	if current_pos>(t-1):
		print "NO"
		break
	elif current_pos==(t-1):
		print "YES"
		break
