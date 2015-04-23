num = [int(char) for char in raw_input()]

if 9-num[0]<num[0] and 9-num[0]!= 0:
	num[0] = 9-num[0]

for i in range(1, len(num)):
	if 9-num[i]<num[i]:
		num[i] = 9-num[i]
resp = 0
num = num[::-1]

for i in range(len(num)):
	resp+=(10**i)*num[i]

print resp
