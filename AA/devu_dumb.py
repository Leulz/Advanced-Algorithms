n, x = map(int, raw_input().split())

subjects = map(int, raw_input().split())

subjects.sort()

total_hours = 0
minus_time = 0
for i in range(n):
	total_hours += subjects[i] * (x - minus_time)
	if x - minus_time>1:
		minus_time+=1

print total_hours
