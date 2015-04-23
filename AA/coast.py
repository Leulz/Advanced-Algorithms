import math

while True:
	try:
		d, vf, vg = map(int, raw_input().split())
	except EOFError:
		break
			
	distance = math.sqrt(d ** 2 + 12 ** 2)

	if 12/float(vf)>=distance/vg:
		print 'S'
	else:
		print 'N'
