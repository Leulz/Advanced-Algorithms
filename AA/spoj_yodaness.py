def merge_and_count(a, b):
	i = 0
	j = 0
	counter = 0
	
	output_list = []
	
	while i < len(a) and j < len(b):
		output_list.append(min(a[i], b[j]))
		if b[j] < a[i]:
			counter += len(a) - i
			j += 1
		else:
			i += 1
	
	if i == len(a):
		for remaining_number in range(j, len(b)):
			output_list.append(b[remaining_number])
	elif j == len(b):
		for remaining_number in range(i, len(a)):
			output_list.append(a[remaining_number])
	
	return counter, output_list

def sort_and_count(array):
	if len(array) == 1:
		return 0, array
	else:
		mid = len(array) // 2
		
		a, b = array[:mid], array[mid:]
		
		ra, a = sort_and_count(a)
		rb, b = sort_and_count(b)
		r, array = merge_and_count(a, b)
		
		return r+ra+rb, array

#n = int(raw_input())

for _ in xrange(int(raw_input())):
        raw_input()
        where_is = {}
        for x, word in enumerate(raw_input().split()):
            where_is[word] = x
        arr = []
        for word in raw_input().split():
            arr.append(where_is[word])
        print sort_and_count(arr)[0]

#for phrase in range(n):
	
	#raw_input()
	
	#yoda_phrase = raw_input()
	#normal_phrase = raw_input()
	
	#word_map = {}
	
	#counter = 1
	
	#normal_list = normal_phrase.split(' ')
	
	#for word in normal_list:
		#word_map[word] = counter
		#counter += 1
	
	#yoda_list = yoda_phrase.split(' ')
	
	#aux_list = [word_map[x] for x in yoda_list]
	
	#print sort_and_count(aux_list)[0]
