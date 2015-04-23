nm = [int(x) for x in raw_input().split()]

n = nm[0]
m = nm[1]

memory = {}

for i in range(n):
	string = raw_input()
	string_size = len(string)
	if string_size not in memory.keys():
		memory[string_size] = []
	memory[string_size].append(string)

for i in range(m):
	query = raw_input()
	query_size = len(query)
	
	if query_size not in memory.keys():
		print 'NO'
	else:
		list_to_query = memory[query_size]
		
		for word_pos in range(len(list_to_query)):
			word = list_to_query[word_pos]
			
			diff_num = 0
			
			for letter in range(len(list_to_query[word_pos])):
				if query[letter] != word[letter]:
					diff_num += 1
			if diff_num == 1:
				print 'YES'
				break
			elif len(list_to_query)-1 == word_pos:
				print 'NO'
			
			
