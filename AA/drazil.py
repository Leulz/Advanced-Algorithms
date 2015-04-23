a, b, s = map(int, raw_input().split())

dist = abs(a)+abs(b)

if s<dist:
	print "No"
else:
	if (s%2==0 and dist%2==1) or (s%2==1 and dist%2==0):
		print "No"
	else:
		print "Yes"
