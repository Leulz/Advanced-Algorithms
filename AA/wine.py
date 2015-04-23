while True:
	n = int(raw_input())
	if n == 0:
		break
	
	street = map(int, raw_input().split())
	ans = 0
	
	for i in range(1, len(street)):
		street[i] += street[i-1]
		ans += abs(street[i-1])
	print ans
