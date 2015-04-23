def numberCards(f):
	return 3*f*(f+1)/2-f

def getMax(n):
	left = 0
	right = 10000000
	while left+1<right:
		mid = (left+right)/2
		if numberCards(mid)<=n:
			left = mid
		else:
			right = mid
	return left

n = int(raw_input())

Max = getMax(n)
while ((Max+n)%3!=0):
	Max-=1
print (Max+3-1)/3
