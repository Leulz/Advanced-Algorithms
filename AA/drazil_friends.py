n, m = map(int,raw_input().split())

boys = map(int, raw_input().split())
boys_to_use = [boys[x] for x in range(1, len(boys))]
total_boys = [False] * n

girls = map(int, raw_input().split())
girls_to_use = [girls[x] for x in range(1, len(girls))]
total_girls = [False] * m

for i in boys_to_use:
	total_boys[i] = True

for i in girls_to_use:
	total_girls[i] = True

days = n * m

boy_counter = boys[0]
girl_counter = girls[0]

flag = False

count = 50
while count>0:
	for i in range(days):
		index_boy = i % n
		index_girl = i % m
		
		if total_boys[index_boy] and not total_girls[index_girl]:
			total_girls[index_girl] = True
			girl_counter += 1
		elif not total_boys[index_boy] and total_girls[index_girl]:
			total_boys[index_boy] = True
			boy_counter += 1
		
		if boy_counter==n and girl_counter==m:
			flag = True
			break
	count -= 1
	if flag:
		break

if flag:
	print "Yes"
else:
	print "No"
