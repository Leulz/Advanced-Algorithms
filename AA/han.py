nxy = [int(x) for x in raw_input().split()]

n = nxy[0]
x = nxy[1]
y = nxy[2]

shots = 0
pd = []

for i in range(n):
	storm = [int(j) for j in raw_input().split()]
	storm_x = storm[0]
	storm_y = storm[1]
	change_x = storm_x - x
	change_y = storm_y - y
	flag = False
	print pd
	print shots
	if change_y == 0:
		for j in pd:
			if j[1] == y:
				flag = True
				break
		if not flag:
			shots+=1
			pd.append((1,y))
			continue
	elif change_x == 0:
		for j in pd:
			if j[0] == x:
				flag = True
				break
		if not flag:
			shots+=1
			pd.append((x,1))
			continue
	else:
		slope = change_y/change_x
		for j in pd:
			if j[0]!=0 and j[1]!=0:
				if storm_x/j[0] == storm_y/j[1]:
					flag = True
					break
		if not flag:
			shots+=1
			pd.append((change_x,slope*(change_x)+y))

print shots
