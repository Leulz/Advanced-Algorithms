n = int(raw_input())
array = [0 for i in range(5000)]

array = [int(x) for x in raw_input().split()]

def menor(l,r):
	menor = 1000000001
	for i in range(l,r):
		if array[i]<menor:
			menor = array[i]	
	return menor

def rec(l,r,h):
	if l>r:
		return 0
	m = menor(l,r)
	retorno = m-h
	flag = False
	comeco = 0
	
	for i in range(l,r+1):		
		if array[i]>m and not flag:
			comeco = i
			flag = True
		elif array[i]==m and flag:
			retorno += rec(comeco,i-1,m)
			flag = False
	
	if flag:
		retorno += rec(comeco,r,m)
	
	return min(retorno,r-l+1)

print rec(0,n-1,0)
