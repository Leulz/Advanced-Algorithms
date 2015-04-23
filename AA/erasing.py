while True:
	n, d = map(int, raw_input().split())
	
	if n==0 and d==0:
		break

	num = map(int, str(raw_input()))
	index_list = [[] for i in range(10)]
	
	for i in range(len(num)):
		index_list[num[i]].append(i)
	
	ans_len = n-d
	curr_index = -1
	ans = []
	
	flag = False
	internal_flag = False
	
	for count in range(n):
		for i in range(len(index_list)-1, -1, -1):
			for j in range(len(index_list[i])):
				if n-(index_list[i][j])>=ans_len and index_list[i][j]>curr_index:
					curr_index = index_list[i][j]
					ans.append(i)
					ans_len -= 1					
					if ans_len==0:
						flag = True
						break
					internal_flag = True
					break
			if flag or internal_flag:
				break
		if flag:
			break
		elif internal_flag:
			internal_flag = False
	print ''.join(map(str,ans))
