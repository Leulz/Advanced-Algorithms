test_cases = int(raw_input())

for test in range(test_cases):
	pac = int(raw_input())
	lista = []
	current_weight = 0
	num_brinq = 0

	for package in range(pac):
		toys, weight = map(int, raw_input().split())

		lista.append([toys/float(weight), toys, weight])

	lista.sort()
	print lista
	for i in range(len(lista)-1, -1, -1):
		if current_weight + lista[i][2]<=50:
			print lista[i]			
			current_weight += lista[i][2]
			print "Weight: %d" % current_weight
			num_brinq += lista[i][1]
	print '---'
	print num_brinq
	print current_weight
	print '---'
