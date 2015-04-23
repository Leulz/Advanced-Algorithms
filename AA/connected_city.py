nm = [int(x) for x in raw_input().split()]

n = nm[0]
m = nm[1]

west_east = raw_input()
north_south = raw_input()

if (west_east[0]=='>' and north_south[-1]=='v' and west_east[-1]=='<' and north_south[0]=='^') or (west_east[0]=='<' and north_south[-1]=='^' and west_east[-1]=='>' and north_south[0]=='v'):
	print "YES"
else:
	print "NO"
