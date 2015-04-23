while True:
	try:
		played_hands = map(int, raw_input().split())
	except EOFError:
		break
	
	if played_hands[0] == played_hands[1] and played_hands[0] == played_hands[2]:
		print "*"
		continue
	if played_hands[0] != played_hands[1] and played_hands[0] != played_hands[2]:
		print "A"
	elif played_hands[1] != played_hands[0] and played_hands[1] != played_hands[2]:
		print "B"
	else:
		print "C"
