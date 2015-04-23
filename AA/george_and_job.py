nmk = [int(x) for x in raw_input().split()]

n = nmk[0]
m = nmk[1]
k = nmk[2]

sequence = [int(x) for x in raw_input().split()]
pd  = []

for i in range(n-m+1):
	counter = 0
	for j in range(m):
		counter += sequence[i+j]
	pd.append((counter,i))

ret = 0

ind = -1

for i in range(k):
	ret+=pd[ind][0]
	ind-=1

print pd
