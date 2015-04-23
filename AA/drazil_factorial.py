n = int(raw_input())

number = list(raw_input())

numbers_seen = [0] * 10

for i in range(len(number)):
	number[i] = int(number[i])
	numbers_seen[number[i]] += 1

ans = []

print numbers_seen

numbers_seen[2] += numbers_seen[3]
numbers_seen[2] += numbers_seen[4]
numbers_seen[2] += numbers_seen[5]
numbers_seen[2] += numbers_seen[6]
numbers_seen[2] += numbers_seen[7]
numbers_seen[2] += numbers_seen[8]
numbers_seen[2] += numbers_seen[9]

print numbers_seen

numbers_seen[3] += numbers_seen[4]
numbers_seen[3] += numbers_seen[5]
numbers_seen[3] += numbers_seen[6]
numbers_seen[3] += numbers_seen[7]
numbers_seen[3] += numbers_seen[8]
numbers_seen[3] += numbers_seen[9]

numbers_seen[4] += numbers_seen[5]
numbers_seen[4] += numbers_seen[6]
numbers_seen[4] += numbers_seen[7]
numbers_seen[4] += numbers_seen[8]
numbers_seen[4] += numbers_seen[9]

numbers_seen[5] += numbers_seen[6]
numbers_seen[5] += numbers_seen[7]
numbers_seen[5] += numbers_seen[8]
numbers_seen[5] += numbers_seen[9]

numbers_seen[6] += numbers_seen[7]
numbers_seen[6] += numbers_seen[8]
numbers_seen[6] += numbers_seen[9]

numbers_seen[7] += numbers_seen[8]
numbers_seen[7] += numbers_seen[9]

numbers_seen[8] += numbers_seen[9]

numbers_seen[3] += numbers_seen[9] * 2
numbers_seen[9] = 0

numbers_seen[2] += numbers_seen[8] * 3
numbers_seen[8] = 0

numbers_seen[6] = 0

numbers_seen[2] += numbers_seen[4] * 2
print numbers_seen
numbers_seen[4] = 0

flag = False
print numbers_seen
if numbers_seen[7] >= 1:
	if numbers_seen[5]<numbers_seen[7] or numbers_seen[3]<2*numbers_seen[7] or numbers_seen[2]<4*numbers_seen[7]:
		flag = True
	else:
		for i in range(numbers_seen[7]):
			numbers_seen[5]-=1
			numbers_seen[3]-=2
			numbers_seen[2]-=4
			ans.append(7)
if numbers_seen[5] >= 1:
	if numbers_seen[3]<numbers_seen[5] or numbers_seen[2]<3*numbers_seen[7]:
		flag = True
	else:
		for i in range(numbers_seen[5]):
			numbers_seen[3]-=1
			numbers_seen[2]-=3
			ans.append(5)
if numbers_seen[3] >= 1:	
	if numbers_seen[2] < numbers_seen[7]:
		flag = True
	else:
		for i in range(numbers_seen[3]):
			ans.append(3)
			numbers_seen[2] -= 1
			
if numbers_seen[2] >= 1:
	for i in range(numbers_seen[2]):
		ans.append(2)

magic = lambda ans: int(''.join(str(i) for i in ans))

if flag:
	print magic(number)
else:	
	ans.sort()
	ans = ans[::-1]
	if magic(ans) > magic(number):
		print magic(ans)
	else:
		print magic(number)
